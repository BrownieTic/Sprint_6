from selenium.webdriver.common.by import By

class Locators:
    # first page order
    input_name = [By.CSS_SELECTOR, 'input[placeholder="* Имя"]']
    input_surname = [By.CSS_SELECTOR, 'input[placeholder="* Фамилия"]']
    input_address = [By.CSS_SELECTOR, 'input[placeholder="* Адрес: куда привезти заказ"]']
    input_metro = [By.CSS_SELECTOR, 'input[placeholder="* Станция метро"]']
    input_phone = [By.CSS_SELECTOR, 'input[placeholder="* Телефон: на него позвонит курьер"]']
    option_metro_first = [By.CSS_SELECTOR, ".select-search__options .select-search__option"]
    button_next = [By.XPATH, './/button[contains(text(),"Далее")]']
    # second page order
    input_date = [By.CSS_SELECTOR, 'input[placeholder="* Когда привезти самокат"]']
    dropdown_rent_period = [By.CLASS_NAME, 'Dropdown-root']
    option_rent_period = [By.XPATH, './/div[text()="сутки"]']
    color_black = [By.ID, 'black']
    color_grey = [By.ID, 'grey']
    button_order_middle = [By.XPATH, './/div[@class="Order_Buttons__1xGrp"]/button[contains(text(),"Заказать")]']
    # window confirmation
    button_yes = [By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Да"]']
    order_confirmation_text = [By.XPATH, '//div[@class="Order_ModalHeader__3FDaJ"]']
