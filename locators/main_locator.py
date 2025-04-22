from selenium.webdriver.common.by import By

class MainPageLocator:
    BUTTON_ORDER_HEADER = (By.XPATH, '//button[@class="Button_Button__ra12g"]')
    BUTTON_ORDER_BIG = (By.XPATH, '//button[@class="Button_Button__ra12g Button_UltraBig__UU3Lp"]')
    BUTTON_YANDEX = (By.XPATH, '//a[@href="//yandex.ru"]')
    BUTTON_SCOOTER = (By.XPATH, '//a[@href="/"]')
    LOGO_DZEN_REDIRECT = (By.XPATH, '//svg[@class="dzen-layout--desktop-base-header__logoWithText-3k dzen-layout--desktop-base-header__isMorda-2n"')