from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.header_locators import Locators as locator_header
from locators.main_page_locators import Locators as locator_main_page

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_on_page(self, locator):
        element = self.driver.find_element(*locator)
        return element

    def click_logo_yandex(self):
        self.click_button(locator_header.logo_yandex)

    def click_logo_scooter(self):
        self.click_button(locator_header.logo_scooter)

    def click_button(self, locator):
        self.find_element_on_page(locator).click()

    def scroll_to_element(self, locator):
        element = self.find_element_on_page(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    
    def find_sibling_element(self, locator):
        element = self.find_element_on_page(locator)
        return element.find_element(*locator_main_page.answer_path).text

    def get_text(self, locator):
        element = self.find_element_on_page(locator)
        return element.text

    def set_value(self, locator, text):
        self.find_element_on_page(locator).send_keys(text)

    def load_url(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_contains(url))

    def wait_to_be_clickable(self, locator): 
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(locator))

    def wait_visibility_of_element(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))

    def click_and_wait_until_is_not_obscured(self, locator):
        element = self.find_element_on_page(locator)
        try: 
            element.click()
        except:  # необходимо для прогрузки элемента, т.к. scooter.png перекрывает клик
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

            element.click()
