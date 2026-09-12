from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page_locators import Locators as locator_main_page
from page.base_page import BasePage

class MainPage(BasePage):

    def click_button_with_scroll(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.wait_to_be_clackable(locator)

        try: 
            element.click()
        except:  # необходимо для прогрузки элемента, т.к. scooter.png перекрывает клик
            self.wait_until_question_is_not_obscured(locator)
            element.click()

    def get_answer_text(self, question_locator):
        element = self.driver.find_element(*question_locator)
        return element.find_element(*locator_main_page.answer_path).text

    def wait_until_question_is_not_obscured(self, locator):
        WebDriverWait(self.driver, 5).until(
            lambda driver: driver.execute_script(
                """
                const element = arguments[0];
                const rect = element.getBoundingClientRect();

                const x = rect.left + rect.width / 2;
                const y = rect.top + rect.height / 2;

                return document.elementFromPoint(x, y) === element;
                """,
                driver.find_element(*locator)
            )
        )