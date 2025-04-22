import allure
import pytest
import data
from pages.questions_page import CheckText

class TestCheckTextAnswer:
    @allure.title('Тест текста ответа на вопрос')
    @pytest.mark.parametrize('question_number, answer_text', data.Questions.questions_list)
    def test_check_text_question(self, driver, question_number, answer_text):
        # arrange
        main_page = CheckText(driver)
        # act
        main_page.scroll_to_question(question_number)
        main_page.wait_clickable(question_number)
        main_page.click_on_question(question_number)
        main_page.wait_text(question_number)
        # assert
        assert main_page.check_answer_on_question(question_number, answer_text)


