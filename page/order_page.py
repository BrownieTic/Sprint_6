from selenium.webdriver.common.keys import Keys

from locators.order_page_locators import Locators as locator
from page.base_page import BasePage

class OrderPage(BasePage):

    def set_name(self, name):
        self.set_value(locator.input_name, name)

    def set_surname(self, surname):
        self.set_value(locator.input_surname, surname)

    def set_address(self, address):
        self.set_value(locator.input_address, address)

    def set_metro(self, metro):
        self.set_value(locator.input_metro, metro)
        self.wait_visibility_of_element(locator.option_metro_first)
        self.click_button(locator.option_metro_first)

    def set_phone(self, phone):
        self.set_value(locator.input_phone, phone)

    def set_date(self, date):
        self.set_value(locator.input_date, date)
        self.find_element_on_page(locator.input_date).send_keys(Keys.ENTER)

    def set_rent_period(self):
        self.click_button(locator.dropdown_rent_period)
        self.wait_visibility_of_element(locator.option_rent_period)
        self.click_button(locator.option_rent_period)   

    def set_color(self, color):
        if color == 'black':
            self.click_button(locator.color_black)
        elif color == 'grey':
            self.click_button(locator.color_grey)

    def click_order_button(self):
        self.click_button(locator.button_order_middle)

    def click_yes_button(self):
        self.click_button(locator.button_yes)

    def get_order_text(self, locator):
        return self.get_text(locator)

    def order(self, name, surname, address, metro, phone, date, color):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_metro(metro)
        self.set_phone(phone)
        self.click_button(locator.button_next)
        self.wait_visibility_of_element(locator.input_date)  

        self.set_date(date)
        self.set_rent_period()
        self.set_color(color)
        self.click_order_button()
        self.wait_visibility_of_element(locator.button_yes)

        self.click_yes_button()
        self.wait_visibility_of_element(locator.order_confirmation_text)        
