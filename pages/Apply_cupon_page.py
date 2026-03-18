from locators.Apply_cupon_locators import CartLocators
from pages.base_page import BasePage

class CartPage(BasePage):

    def open_cart(self):

        self.click(CartLocators.CART_LINK)


    def apply_coupon(self, coupon):

        self.fill(CartLocators.COUPON_CODE, coupon)

        self.click(CartLocators.APPLY_COUPON)


    def get_coupon_error(self):

        return self.get_text(CartLocators.COUPON_ERROR)


    def get_coupon_success_message(self):

        return self.get_text(CartLocators.COUPON_ERROR)


    def checkout(self):

        self.click(CartLocators.CHECKOUT_BUTTON)