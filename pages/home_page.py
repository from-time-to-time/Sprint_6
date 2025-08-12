from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from locators.home_page_locators import HomePageLocators as L
import allure
class HomePage(BasePage):

    @allure.step('Скроллим страницу до раздела FAQ')
    def scroll_to_faq(self):
        self.wait_visible(L.QUESTIONS_SUBTITLE)
        self.scroll_into_view(self.find(L.QUESTIONS_SUBTITLE))
        return self

    @allure.step('Ожидаем отображения всех вопросов раздела FAQ')
    def get_question_items(self):
        return self.wait.until(EC.visibility_of_all_elements_located(L.QUESTIONS))

    @allure.step('Кликаем по вопросу FAQ')
    def click_question_by_index(self, index: int):
        item = self.get_question_items()[index]
        self.scroll_into_view(item)
        button = item.find_element(*L.QUESTION_BUTTON)
        self.wait.until(EC.element_to_be_clickable(button))
        button.click()
        return item
    @allure.step('Ожидаем появления ответа на выбранный вопрос')
    def wait_answer_visible_by_index(self, index: int):
        answer = L.ANSWER_BY_INDEX[index]
        return self.wait.until(EC.visibility_of_element_located(answer))

    @allure.step('Получаем текст ответа FAQ для выбранного вопроса')
    def get_answer_text_by_index(self, index: int):
        answer_text = self.wait_answer_visible_by_index(index)
        return answer_text.text

    @allure.step('Кликаем на верхнюю кнопку "Заказать"')
    def click_up_order_button(self):
        up_button = self.wait_visible(L.UP_ORDER_BUTTON)
        up_button.click()
        return self

    @allure.step('Скроллим до нижней кнопки "Заказать" и кликаем на нее')
    def click_down_order_button(self):
        down_button = self.wait.until(EC.element_to_be_clickable(L.DOWN_ORDER_BUTTON))
        self.scroll_into_view(down_button)
        down_button.click()
        return self