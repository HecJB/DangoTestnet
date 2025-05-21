import asyncio
from pyppeteer import launch

METAMASK_PATH = '/path/to/metamask/extension'  # Update this path

async def launch_browser():
    browser = await launch({
        'headless': False,  # MetaMask UI requires visible browser
        'args': [
            f'--disable-extensions-except={METAMASK_PATH}',
            f'--load-extension={METAMASK_PATH}',
            '--no-sandbox',
            '--disable-setuid-sandbox',
        ],
        'ignoreDefaultArgs': ['--disable-extensions']
    })
    return browser
