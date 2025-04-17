import allure
import curls
from pages.main_page import MainPage

class TestClickLogo:
    @allure.title('Тест клика на лого Яндекса и редиректа на Дзен')
    def test_click_yandex_logo(self, driver):
        # arrange
        main_page = MainPage(driver)
        # act
        main_page.click_yandex_logo()
        main_page.switch_to_new_tab_and_wait()
        # assert
        url_window = main_page.get_url_window()
        assert url_window == curls.url_dzen

    @allure.title('Тест клика на лого Самоката')
    def test_click_scooter_logo(self, driver):
        # arrange
        main_page = MainPage(driver)
        # act
        main_page.click_scooter_logo()
        # assert
        url_window = main_page.get_url_window()
        assert url_window == curls.url_main_pages