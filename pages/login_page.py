from playwright_python_framework_for_DemoWebShop_old_version.pages.base_page import BasePage
from playwright_python_framework_for_DemoWebShop_old_version.locators.login_locators import LoginLocators


class LoginPage(BasePage):

    def click_login_link(self):
        self.click(LoginLocators.LOGIN_LINK)

    def login(self, username, password):

        self.fill(LoginLocators.EMAIL, username)
        self.fill(LoginLocators.PASSWORD, password)
        self.click(LoginLocators.LOGIN_BUTTON)


    def get_error_message(self):

        return self.get_text(LoginLocators.ERROR_MESSAGE)


    def customer_info_validation(self):

        self.wait_for_element(LoginLocators.CUSTOMER_INFO)
        return self.page.locator(LoginLocators.CUSTOMER_INFO).first.is_visible()

    def logout(self):
        self.click(LoginLocators.LOGOUT_BUTTON)