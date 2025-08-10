from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators.base_page_locators import BasePageLocators as L
from config import Config

class BasePage:
    def __init__(self, driver, timeout=Config.TIMEOUT):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url=None):
        if url is None:
            url = Config.URL
        self.driver.get(url)
        return self

    def try_accept_cookies(self):
        try:
            banner = self.wait.until(EC.visibility_of_element_located(L.COOKIE_BANNER))
            try:
                self.wait.until(EC.element_to_be_clickable(L.COOKIE_ACCEPT_BUTTON)).click()
            except TimeoutException:
                self.driver.execute_script("arguments[0].style.display='none';", banner)
        except TimeoutException:
            pass
        return self

    def find(self, locator):
        return self.driver.find_element(*locator)

    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)