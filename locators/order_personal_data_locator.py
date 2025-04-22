from selenium.webdriver.common.by import By

class PersonalDataLocator:
    INPUT_NAME = (By.XPATH, '//input[@placeholder="* Имя"]')
    INPUT_FAMILY = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    INPUT_ADDRESS = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    INPUT_STATION_METRO = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    INPUT_PHONE_NUMBER = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    BUTTON_NEXT = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')

    @staticmethod
    def select_station_metro(station):
        return By.XPATH, f'//button[.="{station}"]'
