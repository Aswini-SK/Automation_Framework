import allure
from pages.Checkout_page import CheckoutPage
from pages.Apply_cupon_page import CartPage
from playwright_python_framework_for_DemoWebShop.pages.login_page import LoginPage


@allure.feature("Checkout")
class TestCheckout:

    def test_checkout_process(self, product_in_cart):
        coupon = CartPage(product_in_cart)
        checkout = CheckoutPage(product_in_cart)

        with allure.step("Open shopping cart"):
            coupon.open_cart()
        with allure.step("Fill billing address"):
            checkout.fill_billing_address(
                country="India",
                city="Hyderabad",
                address="Madhapur",
                zip="500081",
                phone="9876543210"
            )
        # with allure.step("To proceed further"):
        #     checkout.confirm_order()

        with allure.step("Confirm order"):
            checkout.confirm_order()

