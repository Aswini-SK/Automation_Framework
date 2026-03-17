import json

import allure
import pytest

from playwright_python_framework_for_DemoWebShop.pages.login_page import LoginPage


@allure.feature("Login")
class TestLogin:
    with open("test_data/user_credentials.json", "w") as file:
        creds = json.load(file)

    @pytest.mark.parametrize("user", creds)
    @allure.title("Verify login with valid credentials")
    def test_valid_login(self, page, user):


        login = LoginPage(page)

        # Read credentials
        # with open("test_data/user_credentials.json", "w") as file:
        #     creds = json.load(file)
        #
        # email = creds["email"]
        # password = creds["password"]
        # print(email)

        with allure.step("click on Login link"):
            login.click_login_link()

        with allure.step("Login with valid credentials"):
            login.login(user["email"], user["password"])

        with allure.step("Verify application logo"):
            assert login.customer_info_validation()


    @allure.title("Verify login with invalid credentials")
    def test_invalid_login(self, page):

        login = LoginPage(page)

        with allure.step("click on Login link"):
            login.click_login_link()

        with allure.step("Login with invalid credentials"):
            login.login("invalid@email.com", "wrongpassword")

        error = login.get_error_message()

        assert "Login was unsuccessful" in error