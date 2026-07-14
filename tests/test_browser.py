from app.automation.browser import BrowserAutomation

browser = BrowserAutomation()

print(browser.open_website("youtube.com"))
print(browser.open_website("github.com"))
print(browser.open_website("google.com"))