from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from locators.first_order_form_locators import FirstOrderFormLocators as F
from locators.second_order_form_locators import SecondOrderFormLocators as S
import allure

class Order(BasePage):

    @allure.step('Заполняем первую форму заказа: вводим имя={name}, фамилию={surname}, адрес={address}, номер телефона={phone}, выбираем станцию метро={metro}')
    def fill_first_form(self, name, surname, address, metro, phone):
        self.wait_visible(F.NAME_INPUT).send_keys(name)
        self.find(F.SURNAME_INPUT).send_keys(surname)
        self.find(F.ADDRESS_INPUT).send_keys(address)

        inp = self.find(F.METRO_INPUT)
        inp.click()
        self.wait_visible(F.METRO_DROPDOWN)
        inp.send_keys(metro)
        station = self.wait.until(EC.element_to_be_clickable(F.metro_station_value(metro)))
        self.scroll_into_view(station)
        station.click()

        self.find(F.PHONE_INPUT).send_keys(phone)
        return self

    @allure.step('Нажимаем на кнопку "Далее"')
    def click_next_button(self):
        self.wait.until(EC.element_to_be_clickable(F.NEXT_BUTTON)).click()
        return self

    @allure.step('Заполняем вторую форму заказа: выбираем дату={day}, срок аренды="{term_text}", цвет={color}, добавляем комментарий="{comment}"')
    def fill_second_form(self, day, term_text, color, comment):
        self.wait_visible(S.DATE_INPUT).click()
        self.wait_visible(S.CALENDAR)
        date = self.wait.until(EC.element_to_be_clickable(S.date_cell(day)))
        self.scroll_into_view(date)
        date.click()

        self.find(S.RENT_INPUT).click()
        self.wait_visible(S.RENT_MENU)
        term_locator = S.rental_period(term_text)
        self.wait.until(EC.element_to_be_clickable(term_locator)).click()
        color_locator = S.checkbox_color(color)
        self.wait.until(EC.element_to_be_clickable(color_locator)).click()
        self.find(S.COMMENT_INPUT).send_keys(comment)
        return self

    @allure.step('Нажимаем на кнопку "Оформить заказ"')
    def click_order_button(self):
        self.wait.until(EC.element_to_be_clickable(S.ORDER_BUTTON)).click()
        return self
    @allure.step('Нажимаем на кнопку согласия на оформление заказа')
    def agree_to_order(self):
        self.wait_visible(S.ORDER_MODAL)
        self.wait.until(EC.element_to_be_clickable(S.YES_BUTTON)).click()
        return self

    @allure.step('Ожидаем пока появится модальное окно с заголовком успешного оформления заказа')
    def wait_success_modal_header(self):
        return self.wait_visible(S.SUCCESS_ORDER_HEADER)