from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://sauce-demo.myshopify.com/account/login")

    page.fill("#customer_email", "mindpixel168@gmail.com")
    page.fill("#customer_password", "Password1!")
    page.press("#customer_password", "Enter")

    # ✅ VERIFY login success
    page.wait_for_url("**/account**")

    assert "/account" in page.url
    print("✅ Login successful!")

    browser.close()
