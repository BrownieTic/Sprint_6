from page.base_page import BasePage

class MainPage(BasePage):

    def click_button_with_scroll(self, locator):
        self.scroll_to_element(locator)
        self.wait_to_be_clickable(locator)
        self.click_and_wait_until_is_not_obscured(locator)

    def get_answer_text(self, locator):
        return self.find_sibling_element(locator)
