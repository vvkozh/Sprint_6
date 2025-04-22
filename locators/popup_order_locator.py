from selenium.webdriver.common.by import By

class PopupOrderLocator:
    POPUP_ORDER = (By.XPATH, '//div[contains(text(), "Хотите оформить заказ?")]')
    BUTTON_NO = (By.XPATH, '//button[.="Нет"]')
    BUTTON_YES = (By.XPATH, '//button[.="Да"]')
    POPUP_END_ORDER = (By.XPATH, '//div[contains(text(), "Заказ оформлен")]')
    BUTTON_WATCH_ORDER = (By.XPATH, '//button[.="Посмотреть статус"]')
