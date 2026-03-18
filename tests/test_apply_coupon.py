import allure

from playwright_python_framework_for_DemoWebShop_old_version.pages.Apply_cupon_page import CartPage


@allure.feature("Coupon")
class TestCoupon:


    @allure.title("Apply invalid coupon")
    def test_apply_invalid_coupon(self, product_in_cart):

        coupon = CartPage(product_in_cart)

        with allure.step("Open shopping cart"):
            coupon.open_cart()

        with allure.step("Apply invalid coupon code"):
            coupon.apply_coupon("INVALID10")

        error = coupon.get_coupon_error()

        assert "The coupon code you entered couldn't be applied" in error

    @allure.title("Apply empty coupon")
    def test_apply_empty_coupon(self, product_in_cart):
        coupon = CartPage(product_in_cart)

        with allure.step("Open shopping cart"):
            coupon.open_cart()

        with allure.step("Apply empty coupon"):
            coupon.apply_coupon("")

        error = coupon.get_coupon_error()

        assert "The coupon code you entered couldn't be applied" in error

    @allure.title("Apply valid coupon")
    def test_apply_valid_coupon(self, product_in_cart):
        coupon = CartPage(product_in_cart)

        with allure.step("Open shopping cart"):
            coupon.open_cart()

        with allure.step("Apply valid coupon"):
            coupon.apply_coupon("DISCOUNT10")

        message = coupon.get_coupon_error()

        assert "The coupon code you entered couldn't be applied" in message
