import allure
import pytest
import json
import pytest
from playwright_python_framework_for_DemoWebShop.pages.login_page import LoginPage
# from playwright_python_framework.fixtures.browser_fixture import page
from playwright_python_framework_for_DemoWebShop.pages.Product_search_page import SearchPage
from playwright_python_framework_for_DemoWebShop.pages.Add_to_cart_page import ProductPage
import pytest
from playwright_python_framework_for_DemoWebShop.Browser_manager import BrowserManager

import pytest
from playwright.sync_api import sync_playwright

from playwright_python_framework_for_DemoWebShop.config.config_reader import ConfigReader


@pytest.fixture(scope="session")
def config():
    return ConfigReader.read_config()


@pytest.fixture(scope="session")
def env():
    return ConfigReader.read_environment()



@pytest.fixture(scope="function")
def page(config, env):

    playwright, browser, context, page = BrowserManager.launch_browser(config)

    page.goto(env["base_url"])

    yield page

    context.close()
    browser.close()
    playwright.stop()


# @pytest.fixture(scope="function")
# def page(config, env):
#
#     with sync_playwright() as p:
#         browser_name = config["browser"]
#         if browser_name == "chromium":
#             browser = getattr(p, config["browser"]).launch(
#             headless=config["headless"]
#         )
#
#         context = browser.new_context()
#
#         page = context.new_page()
#
#         page.goto(env["base_url"])
#
#         yield page
#
#         context.close()
#         browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:

        page = item.funcargs.get("page")

        if page:

            screenshot = page.screenshot()

            allure.attach(
                screenshot,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )



# login page fixture
@pytest.fixture
def logged_in_page(page):

    login = LoginPage(page)

    # Read credentials
    with open("user_credentials.json") as file:
        creds = json.load(file)

    email = creds["email"]
    password = creds["password"]

    login.click_login_link()
    login.login(email, password)

    return page

# product search and add to cart page fixture
@pytest.fixture
def product_in_cart(logged_in_page):

    search = SearchPage(logged_in_page)
    cart = ProductPage(logged_in_page)

    search.search_product("Laptop")
    search.open_product("14.1-inch Laptop")
    cart.add_to_cart()

    return logged_in_page



