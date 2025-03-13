import time

from selenium.webdriver.common.keys import Keys

from src.data import User
from src.locator.MainLocator import MainLocator
from src.page.CTFPage import CTFPage

class MainPage(CTFPage):
    __action = [
        "*   __click_avatar_image   *",
        "*   __click_logout_item   *",

    ]

    def __init__(self, driver):
        self.locator = MainLocator
        super().__init__(driver)

    def __click_avatar_image(self):
        print(self.__action.__getitem__(0))
        time.sleep(10)
        self.click_element(*self.locator.AVATAR_USER)

    def __click_logout_item(self):
        print(self.__action.__getitem__(1))
        self.click_element(*self.locator.LOG_OUT_ITEM)

    def logout(self):
        self.__click_avatar_image()
        self.__click_logout_item()




