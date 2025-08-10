from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from locators.home_page_locators import HomePageLocators as L
class HomePage(BasePage):

    def scroll_to_faq(self):
        self.wait_visible(L.QUESTIONS_SUBTITLE)
        self.scroll_into_view(self.find(L.QUESTIONS_SUBTITLE))
        return self

    def get_question_items(self):
        return self.wait.until(EC.visibility_of_all_elements_located(L.QUESTIONS))

    def click_question_by_index(self, index: int):
        item = self.get_question_items()[index]
        self.scroll_into_view(item)
        button = item.find_element(*L.QUESTION_BUTTON)
        self.wait.until(EC.element_to_be_clickable(button))
        button.click()
        return item
    def wait_answer_visible_by_index(self, index: int):
        answer = L.ANSWER_BY_INDEX[index]
        return self.wait.until(EC.visibility_of_element_located(answer))

    def get_answer_text_by_index(self, index: int):
        answer_text = self.wait_answer_visible_by_index(index)
        return answer_text.text

    def click_up_order_button(self):
        up_button = self.wait_visible(L.UP_ORDER_BUTTON)
        up_button.click()
        return self

    def click_down_order_button(self):
        down_button = self.wait.until(EC.element_to_be_clickable(L.DOWN_ORDER_BUTTON))
        self.scroll_into_view(down_button)
        down_button.click()
        return self