import allure
from locators.popup_order_locator import PopupOrderLocator
from pages.base_page import BasePage


class PopupOrder(BasePage):
    @allure.step('Нажатие кнопки "Да" на попапе "Хотите оформить заказ?"')
    def click_button_yes_in_popup(self):
        self.click_on_element(PopupOrderLocator.BUTTON_YES)

    @allure.step('Получить текст заголовка попапа')
    def get_text_popup_header(self):
        return self.get_text_on_element(PopupOrderLocator.POPUP_END_ORDER)