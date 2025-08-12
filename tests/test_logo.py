from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators as B
from locators.home_page_locators import HomePageLocators as H
from config import Config
import allure


class TestLogosNavigation:
    @allure.title('Проверка перехода на главную страницу при нажатии на лого "Самокат"')
    def test_logo_samokat_navigates_home(self, driver):
        home = BasePage(driver).open()
        home.try_accept_cookies()
        home.wait_visible(H.UP_ORDER_BUTTON).click()
        home.wait_visible(B.SAMOKAT_LOGO).click()

        assert home.get_current_url() == Config.URL, f"Ожидали {Config.URL}, а получили {home.get_current_url()}"

    @allure.title('Проверка открытия страницы "Дзен" в новой вкладке при нажатии на лого "Яндекс"')
    def test_logo_yandex_opens_dzen_in_new_tab(self, driver):
        home = BasePage(driver).open()

        before = driver.window_handles
        home.wait_visible(B.YANDEX_LOGO).click()

        WebDriverWait(driver, Config.TIMEOUT).until(EC.number_of_windows_to_be(len(before)+1))
        after = driver.window_handles
        assert len(after) == len(before) + 1, "Новая вкладка не открылась"

        driver.switch_to.window(after[-1])
        WebDriverWait(driver, Config.TIMEOUT).until(EC.url_contains("dzen.ru"))
        assert "dzen.ru" in home.get_current_url(), f"Ожидали Дзен, а получили: {home.get_current_url()}"
