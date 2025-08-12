from selenium.webdriver.common.by import By

class BasePageLocators:
    COOKIE_BANNER = (By.XPATH, "(//div[contains(@class, 'App_CookieConsent')])")
    COOKIE_ACCEPT_BUTTON = (By.XPATH, "(//button[contains(@class, 'App_CookieButton')])")
    SAMOKAT_LOGO = (By.XPATH, "(//a[contains(@class, 'Header_LogoScooter')])")
    YANDEX_LOGO = (By.XPATH, "(//a[contains(@class, 'Header_LogoYandex')])")