import allure
import pytest
import curls
import data
from pages.main_page import MainPage
from pages.order_personal_data_page import FillPersonalData
from pages.order_rent_data_page import FillRentData
from pages.popup_order_page import PopupOrder

class TestScooterOrder:
    @allure.title('Тест точки входа в заказ самоката')
    @pytest.mark.parametrize('click_button_method', ["click_button_order_header", "click_button_order_big"])
    def test_different_order_button(self, driver, click_button_method):
        # arrange
        main_page = MainPage(driver)
        # act
        page_order = getattr(main_page, click_button_method)
        page_order()
        # assert
        assert driver.current_url == curls.url_order

    @allure.title('Тест заказа самоката')
    @pytest.mark.parametrize('order_data', data.DataForTest.DataForOrder)
    def test_scooter_order(self, driver, order_data):
        # arrange
        main_page = MainPage(driver)
        main_page.click_button_order_header()
        order_scooter = FillPersonalData(driver)
        order_scooter.filling_field_who_scooter(order_data)
        rent_scooter = FillRentData(driver)
        rent_scooter.filling_rent_data(order_data)
        rent_scooter.select_color_scooter(order_data)
        rent_scooter.click_button_order()
        # act
        popup = PopupOrder(driver)
        popup.click_button_yes_in_popup()
        text_header = popup.get_text_popup_header()
        # assert
        assert 'Заказ оформлен' in text_header



