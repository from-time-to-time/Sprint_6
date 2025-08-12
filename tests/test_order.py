import pytest
from pages.home_page import HomePage
from pages.order_page import Order
from locators.home_page_locators import HomePageLocators as L
import allure

order_test_data = [
    (
        L.UP_ORDER_BUTTON,
        {"name": "Райан", "surname": "Гослинг", "address": "ул. Ленина, 1",
         "metro": "Сокольники", "phone": "79001234567"},
        {"day": 7, "term": "трое суток", "color": "black", "comment": "Позвоните за 10 мин"}
    ),
    (
        L.DOWN_ORDER_BUTTON,
        {"name": "Сальвадор", "surname": "Дали", "address": "ул. Академика Арцимовича, 25",
         "metro": "Фили", "phone": "+79991112233"},
        {"day": 14, "term": "двое суток", "color": "grey", "comment": "Оставьте у консьержа"}
    ),
]

class TestPositiveOrderFlow:

    @pytest.mark.parametrize("button_locator, first, second", order_test_data)
    @allure.title('Проверка оформления заказа самоката')
    def test_order_positive_flow(self, driver, button_locator, first, second):

        home = HomePage(driver).open()
        home.try_accept_cookies()
        home.wait_visible(button_locator).click()

        order = (
            Order(driver)
            .fill_first_form(first["name"], first["surname"], first["address"], first["metro"], first["phone"])
            .click_next_button()
            .fill_second_form(second["day"], second["term"], second["color"], second["comment"])
            .click_order_button()
            .agree_to_order()
        )

        header = order.wait_success_modal_header()
        assert "Заказ оформлен" in header.text, \
            f"Ожидалось 'Заказ оформлен', а получили: {header.text}"