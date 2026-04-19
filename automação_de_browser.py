from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto("https://site.com/login")
    page.fill("#email", "seu@email.com")
    page.fill("#password", "senha")
    page.click("button[type=submit]")

    # Espera elemento aparecer e extrai
    page.wait_for_selector(".dashboard")
    dados = page.inner_text(".dashboard")

    browser.close()
