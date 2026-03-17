import allure

from playwright_python_framework_for_DemoWebShop.pages.Product_search_page import SearchPage
from playwright_python_framework_for_DemoWebShop.utils.data_reader import read_json

data = read_json("test_data/products.json")

@allure.feature("Product Search")
class TestProductSearch:


    @allure.title("Search existing product")
    def test_search_valid_product(self, logged_in_page):

        search = SearchPage(logged_in_page)

        with allure.step("Search for Laptop"):
            search.search_product(data["product"])

        result = search.get_first_search_result()

        assert "Laptop" in result


    @allure.title("Search invalid product")
    def test_search_invalid_product(self, logged_in_page):

        search = SearchPage(logged_in_page)

        with allure.step("Search for invalid product"):
            search.search_product("InvalidProductXYZ")

        message = search.get_no_result_message()

        assert "No products were found" in message