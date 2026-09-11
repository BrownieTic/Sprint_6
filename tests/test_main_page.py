import pytest
import allure

from selenium import webdriver

from urls import Urls as url
from locators.main_page_locators import Locators as locator_main_page
from locators.header_locators import Locators as header_locators
from data import TextDataMainPage as text_data
from page.main_page import MainPage

class TestMainPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.description('Проверка перехода на страницу заказа через кнопки в шапке и на главной странице')
    @pytest.mark.parametrize('button_locator', [
        header_locators.button_order_header,
        locator_main_page.button_order_middle
    ])
    def test_button_order(self, button_locator):
        self.driver.get(url.url_main)
        main_page = MainPage(self.driver)
        main_page.click_button(button_locator)
        assert self.driver.current_url == url.url_order

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
    def test_click_question_show_text(self, question_locator, answer):
        self.driver.get(url.url_main)
        main_page = MainPage(self.driver)
        main_page.click_button(question_locator)
        text_locator = main_page.get_answer_text(question_locator)
        assert text_locator == answer

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
