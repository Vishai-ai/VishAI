from app.browser.browser_manager import BrowserManager

browser = BrowserManager()

print(browser.open_google())

print(browser.open_youtube())

print(browser.search_google("python tutorial"))