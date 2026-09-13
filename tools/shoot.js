/**
 * Drive the atlas in a real browser and take screenshots of it working.
 *
 *   node tools/shoot.js [baseUrl] [outDir]
 *
 * A 3D page that has never been rendered is not finished, and neither WebGL
 * errors nor a cut that fails to load show up in any of the build checks. This
 * walks the page the way a visitor would -- pick a culture, hover a cut, click
 * it, explode the carcass -- and fails loudly if the console reports anything.
 */

const path = require('path');
const fs = require('fs');

const PLAYWRIGHT = process.env.PLAYWRIGHT_PATH ||
  'C:/Users/kk/AppData/Local/npm-cache/_npx/e41f203b7505f1fb/node_modules/playwright';
const { chromium } = require(PLAYWRIGHT);

const base = process.argv[2] || 'http://127.0.0.1:8731/';
const outDir = process.argv[3] || path.join(__dirname, '..', 'build', 'shots');

(async () => {
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await chromium.launch({
    args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'],
  });
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });

  const problems = [];
  page.on('console', m => {
    if (m.type() === 'error' || m.type() === 'warning') problems.push(`${m.type()}: ${m.text()}`);
  });
  page.on('pageerror', e => problems.push(`pageerror: ${e.message}`));
  page.on('requestfailed', r => problems.push(`requestfailed: ${r.url()} ${r.failure()?.errorText}`));

  const shot = async (name, waitMs = 700) => {
    await page.waitForTimeout(waitMs);
    await page.screenshot({ path: path.join(outDir, `${name}.png`) });
    console.log(`shot ${name}`);
  };

  await page.goto(base, { waitUntil: 'networkidle' });
  await page.waitForSelector('#loading', { state: 'hidden', timeout: 45000 });
  await shot('01-open', 1400);

  const cuts = await page.$$('#cut-list li');
  console.log(`legend entries: ${cuts.length}`);

  // click a cut in the legend: the detail panel and the highlight should follow
  await cuts[3].click();
  await page.waitForSelector('#detail:not([hidden])', { timeout: 5000 });
  const selectedName = await page.textContent('.d-native');
  console.log(`selected: ${selectedName}`);
  await shot('02-selected');

  // explode
  await page.fill('#explode', '70');
  await page.dispatchEvent('#explode', 'input');
  await shot('03-exploded', 900);
  await page.fill('#explode', '0');
  await page.dispatchEvent('#explode', 'input');

  // hover a cut in the 3D view itself
  await page.mouse.move(720, 430);
  await page.waitForTimeout(400);
  await page.mouse.move(722, 432);
  await shot('04-hover');

  // every culture in turn, and count what actually arrived in each model
  const tabs = await page.$$('#cultures button');
  const perCulture = [];
  for (let i = 0; i < tabs.length; i++) {
    const label = (await tabs[i].textContent()).trim();
    await tabs[i].click();
    await page.waitForTimeout(1600);
    const counts = await page.evaluate(() => ({
      legend: document.querySelectorAll('#cut-list li').length,
      title: document.getElementById('legend-title').textContent,
    }));
    perCulture.push({ label, ...counts });
    await shot(`05-${String(i + 1).padStart(2, '0')}-${label.replace(/\W+/g, '-').toLowerCase()}`, 300);
  }
  console.table(perCulture);

  await browser.close();

  if (problems.length) {
    console.log('\nCONSOLE PROBLEMS');
    for (const p of [...new Set(problems)]) console.log('  ' + p);
    process.exitCode = 1;
  } else {
    console.log('\nno console errors');
  }
})();
