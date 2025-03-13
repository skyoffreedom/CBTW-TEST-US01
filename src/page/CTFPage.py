import time
from enum import Enum

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from src.utils import Constants


class CTFPage(object):
    def __init__(self, driver, base_url='https://ctflearn.com/'):
        self.base_url = base_url
        self.driver = driver

    def find_element(self, *locator):
        try:
            element = WebDriverWait(self.driver, Constants.MAXIMUM_TIME_OUT).until(ec.visibility_of_element_located(locator)
                                                                              and ec.element_to_be_clickable(locator))
            return element
        except TimeoutException:
            return self.driver.find_element(*locator)

    def find_element_cannot_click(self, *locator):
        try:
            element = WebDriverWait(self.driver, Constants.MAXIMUM_TIME_OUT).until(
                ec.visibility_of_element_located(locator))
            return element
        except TimeoutException:
            return self.driver.find_element(*locator)

    def open(self, url):
        url = self.base_url + url
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def get_current_url_by_tab(self, current_window_handle):
        self.driver.switch_to.window(current_window_handle)
        return self.get_url()

    def click_element(self, *locator):
        element = self.find_element(*locator)
        element.click()
        time.sleep(Constants.MINIMUM_TIME_OUT)

    def click_url_href(self, text):
        element = self.driver.find_element_by_partial_link_text(text)
        element.click()
        time.sleep(Constants.MINIMUM_TIME_OUT)

    def is_existed_element(self, *locator):
        try:
            element = self.find_element(*locator)
            return True
        except Exception:
            return False

    def _switch_to_tab(self, tab_index):
        self.driver.switch_to.window(self.driver.window_handles[tab_index])
        time.sleep(Constants.MINIMUM_TIME_OUT)

    def _switch_to_new_tab(self):
        self.driver.execute_script("window.open('');")
        self._switch_to_tab(1)
        time.sleep(Constants.MAXIMUM_TIME_OUT)