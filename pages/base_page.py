from playwright_python_framework_for_DemoWebShop.utils.logger import get_logger

class BasePage:

    def __init__(self, page):
        self.page = page
        self.logger = get_logger(__name__)


    def click(self, locator):
        self.logger.info(f"Clicking on {locator}")
        self.page.locator(locator).click()


    def fill(self, locator, value):
        self.logger.info(f"Entering text in {locator}")
        self.page.locator(locator).fill(value)


    def check(self, locator):
        self.logger.info(f"checking {locator}")
        self.page.locator(locator).check()


    def get_text(self, locator):
        self.logger.info(f"retrieving the text of {locator}")
        return self.page.locator(locator).text_content()


    def is_visible(self, locator):
        self.logger.info(f"checking visibility of {locator}")
        return self.page.locator(locator).is_visible()


    def wait_for_element(self, locator):
        self.logger.info(f"waiting for {locator}")
        self.page.locator(locator).wait_for(state="visible")


    def select_dropdown(self, locator, value):
        self.logger.info(f"selecting {locator} from dropdown")
        self.page.locator(locator).select_option(value)

    def hover(self, locator):
        self.logger.info(f"Hovering over {locator}")
        self.page.locator(locator).hover()

    def scroll_into_view(self, locator):
        self.logger.info(f"Scrolling to {locator}")
        self.page.locator(locator).scroll_into_view_if_needed()

    def take_screenshot(self, name):
        self.logger.info(f"Taking screenshot {name}")
        self.page.screenshot(path=f"reports/screenshots/{name}.png")