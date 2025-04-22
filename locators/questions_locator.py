from selenium.webdriver.common.by import By

class QuestionsLocator:
    FAQ_LOCATOR = (By.CLASS_NAME, 'Home_FAQ__3uVm4')
    PIC_SCOOTER = (By.XPATH, '//*[@src="/assets/scooter.png"]')

    @staticmethod
    def question_number(number):
        return By.XPATH, f'//*[@id="accordion__heading-{number}"]'

    @staticmethod
    def text_answer(number):
        return By.XPATH, f'//*[@id="accordion__panel-{number}"]/p'
