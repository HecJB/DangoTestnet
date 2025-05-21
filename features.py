async def send_tokens(page):
    # Navigate to Send page or open send modal
    await page.waitForSelector('button#send-tokens')
    await page.click('button#send-tokens')

    # Fill recipient and amount
    await page.waitForSelector('input#recipient-address')
    await page.type('input#recipient-address', '0xRecipientAddressHere')

    await page.type('input#send-amount', '10')  # Example amount

    # Submit send transaction
    await page.click('button#send-submit')

    # Confirm MetaMask transaction popup
    await asyncio.sleep(5)
    pages = await page.browser.pages()
    metamask_popup = None
    for p in pages:
        if 'MetaMask' in await p.title():
            metamask_popup = p
            break

    if metamask_popup:
        await metamask_popup.waitForSelector('button.button-primary')
        await metamask_popup.click('button.button-primary')  # Confirm send

    print("Send transaction submitted.")
