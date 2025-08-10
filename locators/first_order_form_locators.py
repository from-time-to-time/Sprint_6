from selenium.webdriver.common.by import By

class FirstOrderFormLocators:

    NAME_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Имя')]")
    SURNAME_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Фамилия')]")
    ADDRESS_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Адрес')]")
    PHONE_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Телефон')]")

    METRO_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Станция метро')]")
    METRO_DROPDOWN = (By.CSS_SELECTOR, ".select-search__select")

    @staticmethod
    def metro_station_value(metro: str):
        return (
            By.XPATH,
            f"//ul[contains(@class,'select-search__options')]"
            f"//div[contains(@class,'Order_Text') and contains(text(), '{metro}')]"
        )

    NEXT_BUTTON = (By.XPATH, "(//button[contains(@class, 'Button_Middle')])")