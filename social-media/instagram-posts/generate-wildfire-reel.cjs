/**
 * Render the 9:16 wildfire quote into a true animated MP4 reel.
 *
 * Frames are stepped deterministically through the Web Animations API rather
 * than screen-recorded, so timing/exposure is exact and reproducible.
 *
 *   node generate-wildfire-reel.cjs [--frames-only]
 *
 * Output: ../reels/07-wildfire-animated-reel.mp4 (+ thumbnail)
 */
const puppeteer = require('puppeteer-core');
const { execFileSync } = require('child_process');
const fs = require('fs');
const os = require('os');
const path = require('path');

const EDGE = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';
const SOURCE = path.resolve(__dirname, 'quote-wildfire-reel.html');
const REELS_DIR = path.resolve(__dirname, '..', 'reels');
const NAME = '07-wildfire-animated-reel';

const FPS = 30;
const DURATION = 7;          // seconds
const TOTAL_FRAMES = FPS * DURATION;
const W = 1080;
const H = 1920;
const THUMB_AT = 3.6;        // fully-settled frame for the cover

const FRAMES_DIR = path.join(os.tmpdir(), 'opencode-wildfire-reel-frames');

function findFfmpeg() {
  const candidates = [
    process.env.FFMPEG_BIN,
    path.join(
      process.env.LOCALAPPDATA || '',
      'Programs', 'Python', 'Python311', 'Lib', 'site-packages',
      'imageio_ffmpeg', 'binaries', 'ffmpeg-win-x86_64-v7.1.exe'
    ),
    'ffmpeg',
  ].filter(Boolean);

  for (const bin of candidates) {
    try {
      execFileSync(bin, ['-version'], { stdio: 'ignore' });
      return bin;
    } catch {
      /* try next */
    }
  }
  throw new Error('ffmpeg not found — set FFMPEG_BIN');
}

async function render() {
  if (!fs.existsSync(SOURCE)) throw new Error(`Missing source: ${SOURCE}`);

  fs.rmSync(FRAMES_DIR, { recursive: true, force: true });
  fs.mkdirSync(FRAMES_DIR, { recursive: true });
  fs.mkdirSync(REELS_DIR, { recursive: true });

  const browser = await puppeteer.launch({
    headless: true,
    executablePath: EDGE,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu', '--hide-scrollbars'],
  });

  const page = await browser.newPage();
  await page.setViewport({ width: W, height: H, deviceScaleFactor: 1 });
  await page.goto('file://' + SOURCE.replace(/\\/g, '/'), { waitUntil: 'networkidle0' });
  await page.evaluate(() => document.fonts.ready.then(() => true));
  await new Promise((r) => setTimeout(r, 400));

  // Freeze every animation so each frame can be sampled exactly.
  await page.evaluate(() => document.getAnimations().forEach((a) => a.pause()));

  const card = await page.$('.reel');
  const box = await card.boundingBox();
  const clip = {
    x: Math.round(box.x),
    y: Math.round(box.y),
    width: Math.round(box.width),
    height: Math.round(box.height),
  };

  const setTime = (t) =>
    page.evaluate((ms) => {
      document.getAnimations().forEach((a) => {
        a.pause();
        a.currentTime = ms;
      });
    }, t);

  console.log(`Rendering ${TOTAL_FRAMES} frames @ ${FPS}fps from ${path.basename(SOURCE)}…`);

  for (let i = 0; i < TOTAL_FRAMES; i++) {
    await setTime((i * 1000) / FPS);
    await page.screenshot({
      path: path.join(FRAMES_DIR, `frame-${String(i).padStart(4, '0')}.png`),
      clip,
      captureBeyondViewport: false,
    });
    if (i % 30 === 0) process.stdout.write(`  ${i}/${TOTAL_FRAMES}\r`);
  }

  // Thumbnail from the settled frame.
  await setTime(THUMB_AT * 1000);
  const thumbPath = path.join(REELS_DIR, `${NAME}-thumbnail.png`);
  await page.screenshot({ path: thumbPath, clip, captureBeyondViewport: false });

  await browser.close();

  const ffmpeg = findFfmpeg();
  const outPath = path.join(REELS_DIR, `${NAME}.mp4`);

  console.log(`\nEncoding ${NAME}.mp4…`);
  execFileSync(
    ffmpeg,
    [
      '-y',
      '-framerate', String(FPS),
      '-i', path.join(FRAMES_DIR, 'frame-%04d.png'),
      '-c:v', 'libx264',
      '-profile:v', 'high',
      '-pix_fmt', 'yuv420p',
      '-crf', '15',
      '-preset', 'slow',
      // aq-mode=3 biases bitrate toward dark scenes — keeps the gradient from banding
      '-x264-params', 'aq-mode=3:aq-strength=1.1',
      '-movflags', '+faststart',
      outPath,
    ],
    { stdio: ['ignore', 'ignore', 'pipe'] }
  );

  fs.rmSync(FRAMES_DIR, { recursive: true, force: true });

  const mb = (fs.statSync(outPath).size / 1048576).toFixed(1);
  console.log(`  -> reels/${NAME}.mp4 (${mb} MB, ${W}x${H}, ${DURATION}s)`);
  console.log(`  -> reels/${NAME}-thumbnail.png`);
}

render().catch((err) => {
  console.error(err);
  process.exit(1);
});
