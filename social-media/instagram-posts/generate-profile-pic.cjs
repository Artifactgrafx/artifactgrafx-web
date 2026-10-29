const puppeteer = require('puppeteer-core');
const path = require('path');

const EXEC_PATH = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';
const baseDir = __dirname;

async function renderProfilePic() {
  const browser = await puppeteer.launch({
    headless: true,
    executablePath: EXEC_PATH,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu']
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1100, height: 1100 });
  
  const htmlPath = path.resolve(baseDir, 'profile-pic.html');
  await page.goto('file://' + htmlPath, { waitUntil: 'networkidle0' });
  await new Promise(r => setTimeout(r, 1000));
  
  const pic = await page.$('.profile-pic');
  const box = await pic.boundingBox();
  
  await page.screenshot({
    path: path.resolve(baseDir, 'profile-pic.png'),
    clip: { x: box.x, y: box.y, width: Math.round(box.width), height: Math.round(box.height) }
  });
  
  console.log('Saved profile-pic.png (1080x1080)');
  
  await browser.close();
}

renderProfilePic().catch(err => {
  console.error('Error:', err);
});
