import time

import allure

import curls
from locators.main_locator import MainPageLocator
from pages.base_page import BasePage

class MainPage(BasePage):
    @allure.step('Клик на кнопку "Заказать" в хэдере')
    def click_button_order_header(self):
        self.click_on_element(MainPageLocator.BUTTON_ORDER_HEADER)

    @allure.step('Клик на кнопку "Заказать" под описанием')
    def click_button_order_big(self):
        self.scroll_to_element(MainPageLocator.BUTTON_ORDER_BIG)
        self.click_on_element(MainPageLocator.BUTTON_ORDER_BIG)

    @allure.step('Клик на логотип "Яндекс"')
    def click_yandex_logo(self):
        self.click_on_element(MainPageLocator.BUTTON_YANDEX)

    @allure.step('Клик на логотип "Самокат"')
    def click_scooter_logo(self):
        self.click_on_element(MainPageLocator.BUTTON_SCOOTER)

    @allure.step('Ожидание переключения на вторую вкладку')
    def switch_new_window(self):
        self.switch_to_new_tab_and_wait()