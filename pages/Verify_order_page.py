from playwright_python_framework_for_DemoWebShop_old_version.locators.Verify_order_locators import OrderLocators
from playwright_python_framework_for_DemoWebShop_old_version.pages.base_page import BasePage

class OrderPage(BasePage):

    def get_order_success_message(self):

        return self.get_text(OrderLocators.ORDER_SUCCESS)


    def get_order_number(self):

        return self.get_text(OrderLocators.ORDER_NUMBER)