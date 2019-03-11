import asyncio
#from pyppeteer import launch

#async def main():
#    browser = await launch()
#   page = await browser.newPage()
#    await page.goto('http://google.com')
#    await page.screenshot({'path': 'example.png'})
#    await browser.close()

#asyncio.get_event_loop().run_until_complete(main())

async def print_every_second():
    "Print seconds"
    while True:
        for i in range(60):
            print(i, 's')
            await asyncio.sleep(1)


async def print_every_minute():
    for i in range(1, 10):
        await asyncio.sleep(60)
        print(i, 'minute')


loop = asyncio.get_event_loop()
loop.run_until_complete(
    asyncio.gather(print_every_second(),
                   print_every_minute())
)
loop.close()