from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

from locators.order_page_locators import Locators as locator
from locators.header_locators import Locators as locator_header

import time

class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    def click_logo_yandex(self):
        self.driver.find_element(*locator_header.logo_yandex).click()

    def click_logo_scooter(self):
        self.driver.find_element(*locator_header.logo_scooter).click()

    def load_url(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_contains(url))

    def set_name(self, name):
        self.driver.find_element(*locator.input_name).send_keys(name)

    def set_surname(self, surname):
        self.driver.find_element(*locator.input_surname).send_keys(surname)

    def set_address(self, address):
        self.driver.find_element(*locator.input_address).send_keys(address)

    def set_metro(self, metro):
        element = self.driver.find_element(*locator.input_metro)
        element.send_keys(metro)
        self.wait_for_load_order_page(locator.option_metro_first)
        self.driver.find_element(*locator.option_metro_first).click()

    def set_phone(self, phone):
        self.driver.find_element(*locator.input_phone).send_keys(phone)

    def click_next_button(self):
        self.driver.find_element(*locator.button_next).click()

    def set_date(self, date):
        element = self.driver.find_element(*locator.input_date)
        element.send_keys(date)
        element.send_keys(Keys.ENTER)

    def set_rent_period(self):
        element = self.driver.find_element(*locator.dropdown_rent_period)
        element.click()
        self.wait_for_load_order_page(locator.option_rent_period)
        element.find_element(*locator.option_rent_period).click()        

    def set_color(self, color):
        if color == 'black':
            self.driver.find_element(*locator.color_black).click()
        elif color == 'grey':
            self.driver.find_element(*locator.color_grey).click()

    def click_order_button(self):
        self.driver.find_element(*locator.button_order_middle).click()

    def click_yes_button(self):
        self.driver.find_element(*locator.button_yes).click()

    def wait_for_load_order_page(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    def get_order_text(self, locator):
        return self.driver.find_element(*locator).text

    def order(self, name, surname, address, metro, phone, date, color):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_metro(metro)
        self.set_phone(phone)
        self.click_next_button()
        self.wait_for_load_order_page(locator.input_date)  

        self.set_date(date)
        self.set_rent_period()
        self.set_color(color)
        self.click_order_button()
        self.wait_for_load_order_page(locator.button_yes)

        self.click_yes_button()
        self.wait_for_load_order_page(locator.order_confirmation_text)        
