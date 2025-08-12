from selenium.webdriver.common.by import By

class SecondOrderFormLocators:
    DATE_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Когда')]")
    CALENDAR = (By.CSS_SELECTOR, ".react-datepicker")

    @staticmethod
    def date_cell(day: int):
        return (
            By.XPATH,
            f"//div[@role='button' and contains(@class,'react-datepicker__day')"
            f" and not(contains(@class,'--outside-month'))"
            f" and @aria-disabled='false' and normalize-space()='{day}']"
        )

    RENT_INPUT = (By.CLASS_NAME, 'Dropdown-root')
    RENT_MENU = (By.CLASS_NAME, 'Dropdown-menu')
    @staticmethod
    def rental_period(term_text):
        return (By.XPATH, f"//div[contains(@class, 'Dropdown-option') and text() = '{term_text}']")

    @staticmethod
    def checkbox_color(color):
        return (By.XPATH, f"//input[@id = '{color}']")

    COMMENT_INPUT = (By.XPATH, "//input[contains(@placeholder,'Комментарий')]")

    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle') and text() = 'Заказать']")

    ORDER_MODAL = [By.XPATH, "(//div[contains(@class, 'Order_Modal')])[1]"]

    YES_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle') and text() = 'Да']")

    SUCCESS_ORDER_HEADER = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader') and text() = 'Заказ оформлен']")



