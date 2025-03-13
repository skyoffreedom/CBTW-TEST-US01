import time

from src.page.MainPage import MainPage
from src.page.CTFPage import CTFPage
from src.locator.LoginLocator import LoginLocator
from src.utils import Constants


class LoginPage(CTFPage):
    __action = [
        "* __click_login_at_main_page_button *",
        "* __enter_email: {} *",
        "* __enter_password: {} *",
        "* __click_submit_button *",
        "* __verify_error_message: expected: {}, actual: {} *",
    ]

    def __init__(self, driver):
        self.locator = LoginLocator
        super().__init__(driver)

    def __click_login_at_main_page_button(self):
        print(self.__action.__getitem__(0))
        self.click_element(*self.locator.LOGIN_AT_MAIN_PAGE_BUTTON)
        time.sleep(Constants.MAXIMUM_TIME_OUT)

    def __enter_email(self, email):
        print(self.__action.__getitem__(1).format(email))
        self.find_element(*self.locator.EMAIL).send_keys(email)

    def __enter_password(self, password):
        print(self.__action.__getitem__(2).format(password))
        self.find_element(*self.locator.PASSWORD).send_keys(password)

    def __click_submit_button(self):
        print(self.__action.__getitem__(3))
        self.click_element(*self.locator.SUBMIT)
        time.sleep(Constants.MINIMUM_TIME_OUT)

    def __verify_error_message(self, message):
        actual = self.find_element(*self.locator.ERROR_MESSAGE).text
        print(self.__action.__getitem__(4).format(message, actual))
        return True if message in actual else False

    def login(self, email, password):
        self.__click_login_at_main_page_button()
        self.__enter_email(email)
        self.__enter_password(password)
        self.__click_submit_button()

    def re_login(self, email, password):
        self.__enter_email(email)
        self.__enter_password(password)
        self.__click_submit_button()

    def login_with_valid_user(self, email, password):
        self.login(email, password)
        return MainPage(self.driver)

    def re_login_with_valid_user(self, email, password):
        self.re_login(email, password)
        return MainPage(self.driver)

    def login_with_in_valid_user(self, email, password):
        self.login(email, password)
        return self.__verify_error_message("User does not exist for this username")












