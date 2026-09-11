import pytest
import allure

from selenium import webdriver

from urls import Urls as url
from data import TextDataOrderPage as text_data
from data import UserData as user_data
from locators.order_page_locators import Locators as locator
from page.order_page import OrderPage

class TestOrderPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()        

    @allure.description('Заполнение страницы заказа с разными вариантами выбора')
    @pytest.mark.parametrize('name, surname, address, metro, phone, date, color',
        [
        (user_data.user_petr["name"], user_data.user_petr["surname"], user_data.user_petr["address"], user_data.user_petr["metro_station"], user_data.user_petr["phone"], user_data.user_petr["date"], user_data.user_petr["color"]),
        (user_data.user_ivan["name"], user_data.user_ivan["surname"], user_data.user_ivan["address"], user_data.user_ivan["metro_station"], user_data.user_ivan["phone"], user_data.user_ivan["date"], user_data.user_ivan["color"])
        ]
        )
    def test_order(self, name, surname, address, metro, phone, date, color):
        self.driver.get(url.url_order)
        order_page = OrderPage(self.driver)
        order_page.order(name, surname, address, metro, phone, date, color)
        text = order_page.get_order_text(locator.order_confirmation_text)
        assert text_data.order_confirmation_text in text

    @allure.description('Переход на страницу Дзен при нажатие на Яндекс в шапке')
    def test_logo_yandex(self):
        self.driver.get(url.url_order)
        order_page = OrderPage(self.driver)
        current_window = self.driver.current_window_handle
        order_page.click_logo_yandex()
        for window in self.driver.window_handles:
            if window != current_window:
                self.driver.switch_to.window(window)
                break
        order_page.load_url(url.url_dzen)
        assert self.driver.current_url == url.url_dzen

    @allure.description('Переход на главную страницу сервиса при нажатие на Самокат в шапке')
    def test_logo_scooter(self):
        self.driver.get(url.url_order)
        order_page = OrderPage(self.driver)
        order_page.click_logo_scooter()
        order_page.load_url(url.url_main)
        assert self.driver.current_url == url.url_main

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
        