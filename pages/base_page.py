from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators.base_page_locators import BasePageLocators as L
from config import Config
import allure

class BasePage:
    def __init__(self, driver, timeout=Config.TIMEOUT):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step('Открываем главную страницу сайта')
    def open(self, url=None):
        if url is None:
            url = Config.URL
        self.driver.get(url)
        return self

    @allure.step('Соглашаемся с условиями использования cookie-файлов')
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

    @allure.step('Ищем элемент по локатору')
    def find(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Ожидаем, пока элемент станет видимым')
    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step('Скроллим страницу к элементу')
    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Получаем текущий url страницы')
    def get_current_url(self) -> str:
        return self.driver.current_url