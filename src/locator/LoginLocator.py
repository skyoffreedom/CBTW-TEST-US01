from selenium.webdriver.common.by import By


class LoginLocator(object):
    LOGIN_AT_MAIN_PAGE_BUTTON = (By.CSS_SELECTOR, "#navbarSupportedContent > ul > li > a")
    EMAIL = (By.ID, "identifier")
    PASSWORD = (By.ID, "password")
    ERROR_MESSAGE = (By.XPATH, "/html/body/div/div/div/div/div[1]/div[2]/form/div[1]/div")
    SUBMIT = (By.XPATH, "/html/body/div/div/div/div/div[1]/div[2]/form/button")
    
