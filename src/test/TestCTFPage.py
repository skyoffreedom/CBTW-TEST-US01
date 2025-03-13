from selenium.webdriver.chrome.service import Service

from src.utils import Constants
from selenium import webdriver
import time
import unittest

from src.data import Settings


class TestCTFPage(unittest.TestCase):
    def setUp(self):
        service = Service()
        if Settings.HIDE_UI:
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('window-size=1980x1080')
            options.add_argument('--disable-dev-shm-usage')
            self.driver = webdriver.Chrome(service=service, options=options)
        else:
            options = webdriver.ChromeOptions()
            self.driver = webdriver.Chrome()
            self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.get(Constants.END_POINT)
        self.driver.maximize_window()
        time.sleep(Constants.MINIMUM_TIME_OUT)

    def tearDown(self):
        time.sleep(Constants.MINIMUM_TIME_OUT)
        self.driver.quit()
        if hasattr(self, 'driver1'):
            self.driver1.quit()

    def openIncognito(self):
        if Settings.HIDE_UI:
            options1 = webdriver.ChromeOptions()
            options1.add_argument('--headless')
            options1.add_argument('--no-sandbox')
            options1.add_argument('window-size=1980x1080')
            options1.add_argument("--incognito")
            options1.add_argument('--disable-dev-shm-usage')
            self.driver1 = webdriver.Chrome(options=options1)
        else:
            options1 = webdriver.ChromeOptions()
            options1.add_argument('--incognito')
            self.driver1 = webdriver.Chrome(options=options1)

        self.driver1.get(Constants.END_POINT)
        self.driver1.maximize_window()
        time.sleep(Constants.MINIMUM_TIME_OUT)
