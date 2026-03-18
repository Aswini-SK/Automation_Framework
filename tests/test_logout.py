import allure

from playwright_python_framework_for_DemoWebShop_old_version.pages.login_page import LoginPage


@allure.feature("Logout")
class TestLogout:


    @allure.title("Verify user logout")
    def test_logout(self, logged_in_page):
        login = LoginPage(logged_in_page)

        login.logout()

        assert "Log in" in logged_in_page.content()