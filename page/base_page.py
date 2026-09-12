from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.header_locators import Locators as locator_header

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_logo_yandex(self):
        self.click_button(locator_header.logo_yandex)

    def click_logo_scooter(self):
        self.click_button(locator_header.logo_scooter)

    def click_button(self, locator):
        self.driver.find_element(*locator).click()

    def load_url(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_contains(url))

    def wait_to_be_clackable(self, locator): 
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(locator))

    def wait_visibility_of_element(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))
