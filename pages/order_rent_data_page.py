import allure
from locators.order_rent_data_locator import RentDataLocator
from pages.base_page import BasePage

class FillRentData(BasePage):

    @allure.step('Заполнение полей на странице "Про аренду"')
    def filling_rent_data(self, order_data):
        self.send_keys_to_input(RentDataLocator.INPUT_DATE, order_data['date'])
        self.click_on_element(RentDataLocator.SELECT_DATE_CALENDAR)
        self.click_on_element(RentDataLocator.INPUT_RENTAL_TIME)
        self.click_on_element(RentDataLocator.select_rental_time_locator(order_data['time_rent']))
        self.send_keys_to_input(RentDataLocator.INPUT_COMMENT, order_data['comment'])

    @allure.step('Выбор цвета самоката')
    def select_color_scooter(self, order_data):
        if len(order_data['color']) == 1:
            color_scooter = order_data['color']
            self.click_on_element(RentDataLocator.select_color_locator(color_scooter[0]))
        elif len(order_data['color']) == 2:
            color_scooter = order_data['color']
            self.click_on_element(RentDataLocator.select_color_locator(color_scooter[0]))
            self.click_on_element(RentDataLocator.select_color_locator(color_scooter[1]))

    @allure.step('Клик на кнопку "Заказать"')
    def click_button_order(self):
        self.click_on_element(RentDataLocator.BUTTON_ORDER)