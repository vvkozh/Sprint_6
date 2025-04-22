from selenium.webdriver.common.by import By

class RentDataLocator:
    INPUT_DATE = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    INPUT_RENTAL_TIME = (By.XPATH, '//*[.="* Срок аренды"]')
    SELECT_DATE_CALENDAR = (By.XPATH, '//div[@class="react-datepicker__week"]/div[@tabindex="0"]')

    INPUT_COMMENT = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    BUTTON_BACK = (By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[@class="Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i"]')
    BUTTON_ORDER = (By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')

    @staticmethod
    def select_rental_time_locator(time):
        return By.XPATH, f'//div[@class="Dropdown-menu"]/div[.="{time}"]'

    @staticmethod
    def select_color_locator(color):
        return By.XPATH, f'//label[@for="{color}"]'
