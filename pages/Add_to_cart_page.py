from playwright_python_framework_for_DemoWebShop_old_version.locators.Add_to_cart_locators import ProductLocators
from playwright_python_framework_for_DemoWebShop_old_version.pages.base_page import BasePage

class ProductPage(BasePage):

    def add_to_cart(self):

        self.click(ProductLocators.ADD_TO_CART)
    def product_status(self):
        return self.get_text(ProductLocators.PRODUCT_STATUS)