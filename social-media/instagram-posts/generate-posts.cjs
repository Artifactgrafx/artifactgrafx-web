const puppeteer = require('puppeteer-core');
const path = require('path');
const fs = require('fs');

const EXEC_PATH = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';
const baseDir = __dirname;

async function renderCarousel() {
  const browser = await puppeteer.launch({
    headless: true,
    executablePath: EXEC_PATH,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu']
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1200, height: 2000 });
  
  const htmlPath = path.resolve(baseDir, 'carousel.html');
  await page.goto('file://' + htmlPath, { waitUntil: 'networkidle0' });
  await new Promise(r => setTimeout(r, 1000));
  
  const slides = await page.$$('.slide');
  console.log(`Found ${slides.length} carousel slides`);
  
  for (let i = 0; i < slides.length; i++) {
    const box = await slides[i].boundingBox();
    if (!box) continue;
    await page.screenshot({
      path: path.resolve(baseDir, 'carousel', `slide-${i + 1}.png`),
      clip: { x: box.x, y: box.y, width: Math.round(box.width), height: Math.round(box.height) }
    });
    console.log(`Saved carousel/slide-${i + 1}.png`);
  }
  
  await browser.close();
}

async function renderQuoteCards() {
  const browser = await puppeteer.launch({
    headless: true,
    executablePath: EXEC_PATH,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu']
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1200, height: 2000 });
  
  const htmlPath = path.resolve(baseDir, 'quote-cards.html');
  await page.goto('file://' + htmlPath, { waitUntil: 'networkidle0' });
  await new Promise(r => setTimeout(r, 1000));
  
  const cards = await page.$$('.quote-card');
  console.log(`Found ${cards.length} quote cards`);
  
  for (let i = 0; i < cards.length; i++) {
    const box = await cards[i].boundingBox();
    if (!box) continue;
    await page.screenshot({
      path: path.resolve(baseDir, 'quote-cards', `quote-${i + 1}.png`),
      clip: { x: box.x, y: box.y, width: Math.round(box.width), height: Math.round(box.height) }
    });
    console.log(`Saved quote-cards/quote-${i + 1}.png`);
  }
  
  await browser.close();
}

async function renderStoryPosts() {
  const browser = await puppeteer.launch({
    headless: true,
    executablePath: EXEC_PATH,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu']
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1200, height: 2100 });
  
  const htmlPath = path.resolve(baseDir, 'story-posts.html');
  await page.goto('file://' + htmlPath, { waitUntil: 'networkidle0' });
  await new Promise(r => setTimeout(r, 1000));
  
  const stories = await page.$$('.story');
  console.log(`Found ${stories.length} story posts`);
  
  for (let i = 0; i < stories.length; i++) {
    const box = await stories[i].boundingBox();
    if (!box) continue;
    await page.screenshot({
      path: path.resolve(baseDir, 'story-posts', `story-${i + 1}.png`),
      clip: { x: box.x, y: box.y, width: Math.round(box.width), height: Math.round(box.height) }
    });
    console.log(`Saved story-posts/story-${i + 1}.png`);
  }
  
  await browser.close();
}

async function main() {
  try {
    await renderCarousel();
    await renderQuoteCards();
    await renderStoryPosts();
    console.log('\nAll done! Check the instagram-posts folder.');
  } catch (err) {
    console.error('Error:', err);
  }
}

main();
