import pytest
import allure

from urls import Urls as url
from locators.main_page_locators import Locators as locator_main_page
from locators.header_locators import Locators as header_locators
from data import TextDataMainPage as text_data
from page.main_page import MainPage

class TestMainPage:
    
    @allure.description('Проверка перехода на страницу заказа через кнопки в шапке и на главной странице')
    @pytest.mark.parametrize('button_locator', [
        header_locators.button_order_header,
        locator_main_page.button_order_middle
    ])
    def test_button_order(self, driver_main_page, button_locator):
        main_page = MainPage(driver_main_page)
        main_page.click_button_with_scroll(button_locator)
        assert driver_main_page.current_url == url.URL_ORDER

    @allure.description('Проверка открытия ответа и его текста при нажатие на вопрос')
    @pytest.mark.parametrize('question_locator, answer', [
        (locator_main_page.question_1, text_data.answer_1),
        (locator_main_page.question_2, text_data.answer_2),
        (locator_main_page.question_3, text_data.answer_3),
        (locator_main_page.question_4, text_data.answer_4),
        (locator_main_page.question_5, text_data.answer_5),
        (locator_main_page.question_6, text_data.answer_6),
        (locator_main_page.question_7, text_data.answer_7),
        (locator_main_page.question_8, text_data.answer_8)
    ])
    def test_click_question_show_text(self, driver_main_page, question_locator, answer):
        main_page = MainPage(driver_main_page)
        main_page.click_button_with_scroll(question_locator)
        text_locator = main_page.get_answer_text(question_locator)
        assert text_locator == answer
