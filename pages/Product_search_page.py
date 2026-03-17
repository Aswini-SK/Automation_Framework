from playwright_python_framework_for_DemoWebShop.pages.base_page import BasePage
from playwright_python_framework_for_DemoWebShop.locators.Product_search_locators import SearchLocators


class SearchPage(BasePage):

    def search_product(self, product):

        self.fill(SearchLocators.SEARCH_BOX, product)
        self.click(SearchLocators.SEARCH_BUTTON)


    def open_product(self, product):

        self.click(SearchLocators.PRODUCT_LINK.format(product))


    def get_first_search_result(self):

        return self.get_text(SearchLocators.SEARCH_RESULT_PRODUCT)


    def get_no_result_message(self):

        return self.get_text(SearchLocators.NO_RESULT_MESSAGE)