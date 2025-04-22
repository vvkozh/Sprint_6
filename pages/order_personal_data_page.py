import allure
from locators.order_personal_data_locator import PersonalDataLocator
from pages.base_page import BasePage

class FillPersonalData(BasePage):
    @allure.step('Заполнение полей на странице "Для кого самокат"')
    def filling_field_who_scooter(self, order_data):
        self.send_keys_to_input(PersonalDataLocator.INPUT_NAME, order_data['name'])
        self.send_keys_to_input(PersonalDataLocator.INPUT_FAMILY, order_data['family'])
        self.send_keys_to_input(PersonalDataLocator.INPUT_ADDRESS, order_data['address'])
        self.click_on_element(PersonalDataLocator.INPUT_STATION_METRO)
        self.click_on_element(PersonalDataLocator.select_station_metro(order_data['station_metro']))
        self.send_keys_to_input(PersonalDataLocator.INPUT_PHONE_NUMBER, order_data['phone_number'])
        self.click_on_element(PersonalDataLocator.BUTTON_NEXT)