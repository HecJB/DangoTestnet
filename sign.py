async def dango_signup(page):
    await page.goto('http://test-portal.dango.exchange/signup', {'waitUntil': 'networkidle2'})

    # Click "Sign Up with Wallet" button (update selector)
    await page.waitForSelector('button#sign-up-with-wallet')
    await page.click('button#sign-up-with-wallet')

    # Wait for MetaMask popup and approve connection
    await asyncio.sleep(5)
    pages = await page.browser.pages()
    metamask_popup = None
    for p in pages:
        if 'MetaMask' in await p.title():
            metamask_popup = p
            break

    if metamask_popup:
        await metamask_popup.waitForSelector('button.button-primary')
        await metamask_popup.click('button.button-primary')  # Approve connection

    # Back to main page, enter username
    await page.bringToFront()
    await page.waitForSelector('input#username')
    await page.type('input#username', 'your_username_here')

    # Check availability and create username
    await page.click('button#check-username')
    await page.waitForSelector('div#username-available', timeout=5000)
    await page.click('button#create-account')

    # Confirm transaction in MetaMask popup
    await asyncio.sleep(5)
    pages = await page.browser.pages()
    for p in pages:
        if 'MetaMask' in await p.title():
            metamask_popup = p
            break

    if metamask_popup:
        await metamask_popup.waitForSelector('button.button-primary')
        await metamask_popup.click('button.button-primary')  # Confirm transaction

    print("Username created successfully.")
