from playwright_python_framework_for_DemoWebShop_old_version.locators.Checkout_locators import CheckoutLocators
from playwright_python_framework_for_DemoWebShop_old_version.pages.base_page import BasePage

class CheckoutPage(BasePage):

    def fill_billing_address(self, country, city, address, zip, phone):
        self.check(CheckoutLocators.ACCEPT_TERMS_AD_SERVICES)
        self.click(CheckoutLocators.CHECKOUT_BUTTON)

        if CheckoutLocators.EXISTING_BILLING_ADDRESS:
            self.click(CheckoutLocators.EXISTING_CONTINUE_BUTTON)

        else:
            self.select_dropdown(CheckoutLocators.COUNTRY, country)

            self.fill(CheckoutLocators.CITY, city)

            self.fill(CheckoutLocators.ADDRESS, address)

            self.fill(CheckoutLocators.ZIP, zip)

            self.fill(CheckoutLocators.PHONE, phone)


    def confirm_order(self):
        self.click(CheckoutLocators.PICKUP)
        self.click(CheckoutLocators.SHIPPING)
        self.click(CheckoutLocators.PAYMENT_TYPE)
        self.click(CheckoutLocators.PAYMENT_INFO)
        self.click(CheckoutLocators.CONFIRM_ORDER)
        self.click(CheckoutLocators.CONTINUE_FURTHER)

        # self.click(CheckoutLocators.CONFIRM_ORDER)