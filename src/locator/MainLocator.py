from selenium.webdriver.common.by import By


class MainLocator(object):
    AVATAR_USER = (By.CSS_SELECTOR, "#profileDropdown > img")
    LOG_OUT_ITEM = (By.CSS_SELECTOR, "#navbarSupportedContent > ul > li.nav-item.dropleft.show > div > a:nth-child(7)")
