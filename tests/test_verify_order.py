import allure

from playwright_python_framework_for_DemoWebShop_old_version.pages.Verify_order_page import OrderPage


@allure.feature("Order")
class TestVerifyOrder:


    @allure.title("Verify order placed successfully")
    def test_verify_order(self, page):

        order = OrderPage(page)

        message = order.get_order_success_message()

        assert "Your order has been successfully processed!" in message

    @allure.title("Verify order placed successfully")
    def test_verify_order(self, page):
        order = OrderPage(page)

        success_message = order.get_order_success_message()

        order_number = order.get_order_number()

        assert success_message == "Your order has been successfully processed!"

        assert "Order number:" in order_number