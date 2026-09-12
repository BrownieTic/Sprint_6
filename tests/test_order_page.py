import pytest
import allure

from urls import Urls as url
from data import TextDataOrderPage as text_data
from data import UserData as user_data
from locators.order_page_locators import Locators as locator
from page.order_page import OrderPage

class TestOrderPage:   

    @allure.description('Заполнение страницы заказа с разными вариантами выбора')
    @pytest.mark.parametrize('name, surname, address, metro, phone, date, color',
        [
        (user_data.user_petr["name"], user_data.user_petr["surname"], user_data.user_petr["address"], user_data.user_petr["metro_station"], user_data.user_petr["phone"], user_data.user_petr["date"], user_data.user_petr["color"]),
        (user_data.user_ivan["name"], user_data.user_ivan["surname"], user_data.user_ivan["address"], user_data.user_ivan["metro_station"], user_data.user_ivan["phone"], user_data.user_ivan["date"], user_data.user_ivan["color"])
        ]
        )
    def test_order(self, driver_order_page, name, surname, address, metro, phone, date, color):
        order_page = OrderPage(driver_order_page)
        order_page.order(name, surname, address, metro, phone, date, color)
        text = order_page.get_order_text(locator.order_confirmation_text)
        assert text_data.order_confirmation_text in text

    @allure.description('Переход на страницу Дзен при нажатие на Яндекс в шапке')
    def test_logo_yandex(self, driver_order_page):
        order_page = OrderPage(driver_order_page)
        order_page.click_logo_yandex()
        for window in driver_order_page.window_handles:
            driver_order_page.switch_to.window(window)
        order_page.load_url(url.URL_DZEN)
        assert driver_order_page.current_url == url.URL_DZEN

    @allure.description('Переход на главную страницу сервиса при нажатие на Самокат в шапке')
    def test_logo_scooter(self, driver_order_page):
        order_page = OrderPage(driver_order_page)
        order_page.click_logo_scooter()
        order_page.load_url(url.URL_MAIN)
        assert driver_order_page.current_url == url.URL_MAIN
        