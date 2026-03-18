import allure
import json
from faker import Faker
from pages.Registration_Page import RegistrationPage

fake = Faker()

@allure.feature("User Registration")
class TestRegistration:

    @allure.title("Register user successfully")
    def test_register_user(self, page):

        register = RegistrationPage(page)

        email = fake.email()
        password = "Password@123"

        with allure.step("click on registration link"):
            register.click_register_link()

        with allure.step("Select gender"):
            register.select_gender("male")

        with allure.step("Enter first name"):
            register.enter_first_name(fake.first_name())

        with allure.step("Enter last name"):
            register.enter_last_name(fake.last_name())

        with allure.step("Enter email"):
            register.enter_email(email)

        with allure.step("Enter password"):
            register.enter_password(password)

        with allure.step("Confirm password"):
            register.confirm_password(password)

        with allure.step("Click register"):
            register.click_register()

        assert "Your registration completed" in page.content()

        # Save credentials for login test
        creds = {
            "email": email,
            "password": password
        }

        with open("test_data/user_credentials.json", "w") as file:
            json.dump(creds, file, indent=4)