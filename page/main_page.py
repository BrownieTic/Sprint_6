from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page_locators import Locators as locator_main_page

import time

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_load(self, question_locator): 
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(question_locator))

    def click_button(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.wait_for_load(locator)

        try: 
            element.click()
        except:  # необходимо для прогрузки элемента, т.к. scooter.png перекрывает клик
            time.sleep(0.3)
            element.click()

    def get_answer_text(self, question_locator):
        element = self.driver.find_element(*question_locator)
        return element.find_element(*locator_main_page.answer_path).text
        