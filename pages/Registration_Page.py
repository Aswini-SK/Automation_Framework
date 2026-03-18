from pages.base_page import BasePage
from locators.Registration_locators import RegistrationLocators


class RegistrationPage(BasePage):

    def click_register_link(self):
        self.click(RegistrationLocators.REGISTRATION_LINK)

    def select_gender(self, gender):

        self.check(RegistrationLocators.GENDER.format(gender.lower()))


    def enter_first_name(self, firstname):

        self.fill(RegistrationLocators.FIRST_NAME, firstname)


    def enter_last_name(self, lastname):

        self.fill(RegistrationLocators.LAST_NAME, lastname)


    def enter_email(self, email):

        self.fill(RegistrationLocators.EMAIL, email)


    def enter_password(self, password):

        self.fill(RegistrationLocators.PASSWORD, password)


    def confirm_password(self, password):

        self.fill(RegistrationLocators.CONFIRM_PASSWORD, password)


    def click_register(self):

        self.click(RegistrationLocators.REGISTER_BUTTON)