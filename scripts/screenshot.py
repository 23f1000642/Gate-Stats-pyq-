import asyncio, sys
from playwright.async_api import async_playwright
async def route(r):
    u=r.request.url
    if 'marked' in u: await r.fulfill(path='npm/node_modules/marked/marked.min.js', content_type='application/javascript')
    elif 'mathjax' in u: await r.fulfill(path='npm/node_modules/mathjax/es5/tex-svg.js', content_type='application/javascript')
    else: await r.abort()
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={'width':1280,'height':1600})
        await pg.route('**/cdnjs.cloudflare.com/**', route)
        errs=[]; pg.on('console', lambda m: errs.append(m.text) if m.type=='error' else None)
        await pg.goto('http://localhost:8765/index.html#'+sys.argv[1]); await pg.wait_for_timeout(4000)
        await pg.screenshot(path='build/shot.png')
        await pg.click('[data-tab=p]'); await pg.wait_for_timeout(800); await pg.screenshot(path='build/shot_p.png')
        await pg.click('[data-tab=f]'); await pg.wait_for_timeout(2500); await pg.screenshot(path='build/shot_f.png')
        m=await b.new_page(viewport={'width':400,'height':1400}); await m.route('**/cdnjs.cloudflare.com/**', route)
        await m.goto('http://localhost:8765/index.html#'+sys.argv[1]); await m.wait_for_timeout(3000)
        await m.screenshot(path='build/shot_m.png')
        print('errors',errs)
        await b.close()
asyncio.run(main())
