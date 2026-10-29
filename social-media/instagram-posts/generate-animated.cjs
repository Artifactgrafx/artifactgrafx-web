const puppeteer = require('puppeteer-core');
const path = require('path');

const EXEC_PATH = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';
const baseDir = __dirname;

async function render(htmlFile, outputName) {
  const browser = await puppeteer.launch({
    headless: true,
    executablePath: EXEC_PATH,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu']
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1200, height: 2000 });
  
  const htmlPath = path.resolve(baseDir, htmlFile);
  await page.goto('file://' + htmlPath, { waitUntil: 'networkidle0' });
  await new Promise(r => setTimeout(r, 2500));
  
  const card = await page.$('.quote-card');
  const box = await card.boundingBox();
  
  await page.screenshot({
    path: path.resolve(baseDir, 'quote-cards', outputName),
    clip: { x: box.x, y: box.y, width: Math.round(box.width), height: Math.round(box.height) }
  });
  
  console.log(`Saved quote-cards/${outputName}`);
  
  await browser.close();
}

async function main() {
  try {
    await render('quote-wildfire-animated.html', 'quote-4-wildfire-animated.png');
    await render('quote-dig-animated.html', 'quote-5-dig-ideas-animated.png');
    console.log('\nAll done!');
  } catch (err) {
    console.error('Error:', err);
  }
}

main();
