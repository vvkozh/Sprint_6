import allure
from locators.questions_locator import QuestionsLocator
from pages.base_page import BasePage

class CheckText(BasePage):

    @allure.step('Скролл до вопроса')
    def scroll_to_question(self, question_number):
        question_locator = QuestionsLocator.question_number(question_number)
        self.scroll_to_element(question_locator)

    @allure.step('Подождать когда вопрос будет кликабелен')
    def wait_clickable(self, question_number):
        question_locator = QuestionsLocator.question_number(question_number)
        self.wait_clickable_element(question_locator)

    @allure.step('Подождать текст в ответе на вопрос')
    def wait_text(self, question_number):
        question_locator = QuestionsLocator.text_answer(question_number)
        self.wait_for_element(question_locator)

    @allure.step('Открыть ответ на вопрос')
    def click_on_question(self, question_number):
        question_locator = QuestionsLocator.question_number(question_number)
        self.click_on_element(question_locator)

    @allure.step('Сравнить ответ на вопрос')
    def check_answer_on_question(self, question_number, expected_text):
        actual_text = self.get_text_on_element(QuestionsLocator.text_answer(question_number))
        return actual_text == expected_text
