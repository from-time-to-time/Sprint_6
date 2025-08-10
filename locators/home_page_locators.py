from selenium.webdriver.common.by import By
class HomePageLocators:
    QUESTIONS_SUBTITLE = (By.XPATH, "(//div[contains(@class,'Home_SubHeader')])[4]")
    QUESTIONS = (By.CLASS_NAME, "accordion__item")
    QUESTION_BUTTON = (By.CSS_SELECTOR, ".accordion__button")

    ANSWER_BY_INDEX = {
        0: (By.ID, "accordion__panel-0"),
        1: (By.ID, "accordion__panel-1"),
        2: (By.ID, "accordion__panel-2"),
        3: (By.ID, "accordion__panel-3"),
        4: (By.ID, "accordion__panel-4"),
        5: (By.ID, "accordion__panel-5"),
        6: (By.ID, "accordion__panel-6"),
        7: (By.ID, "accordion__panel-7"),
                }
    UP_ORDER_BUTTON = (By.XPATH, "(//button[contains(@class, 'Button_Button')])[1]")
    DOWN_ORDER_BUTTON = (By.XPATH, "(//button[contains(@class, 'Button_Middle')])")