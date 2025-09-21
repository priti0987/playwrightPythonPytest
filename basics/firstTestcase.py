from playwright.sync_api import sync_playwright,Playwright,expect

def run(playwright:Playwright) ->None:
    browser =playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page=context.new_page()

    page.goto("https://www.google.com")
    # print(page.get_by_title())
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)