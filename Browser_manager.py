from playwright.sync_api import sync_playwright


class BrowserManager:

    @staticmethod
    def launch_browser(config):

        playwright = sync_playwright().start()

        browser_name = config["browser"]

        if browser_name == "chromium":
            browser = playwright.chromium.launch(headless=config["headless"])

        elif browser_name == "firefox":
            browser = playwright.firefox.launch(headless=config["headless"])

        else:
            browser = playwright.webkit.launch(headless=config["headless"])

        context = browser.new_context()

        page = context.new_page()

        return playwright, browser, context, page