from selenium import webdriver
browser = None

def get_browser(binary=None, proxy=None):
    global browser
    if not browser:
        browser = webdriver.Firefox(firefox_binary=binary, proxy=proxy)
    return browser