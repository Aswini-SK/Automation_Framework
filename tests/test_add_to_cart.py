import allure

from playwright_python_framework_for_DemoWebShop.pages.Product_search_page import SearchPage
from playwright_python_framework_for_DemoWebShop.pages.Add_to_cart_page import ProductPage


@allure.feature("Shopping Cart")
class TestAddToCart:


    @allure.title("Add product to cart")
    def test_add_product_to_cart(self, page):

        search = SearchPage(page)
        cart = ProductPage(page)

        with allure.step("Search product"):
            search.search_product("Laptop")

        with allure.step("Open product"):
            search.open_product("14.1-inch Laptop")

        with allure.step("Add product to cart"):
            cart.add_to_cart()

        message = cart.product_status()

        assert "The product has been added to your shopping cart" in message
