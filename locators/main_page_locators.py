from selenium.webdriver.common.by import By

class Locators:
    # section with questions
    question_1 = [By.ID, 'accordion__heading-0']
    question_2 = [By.ID, 'accordion__heading-1']
    question_3 = [By.ID, 'accordion__heading-2']
    question_4 = [By.ID, 'accordion__heading-3']
    question_5 = [By.ID, 'accordion__heading-4']
    question_6 = [By.ID, 'accordion__heading-5']
    question_7 = [By.ID, 'accordion__heading-6']
    question_8 = [By.ID, 'accordion__heading-7']
    answer_path = [By.XPATH, '../following-sibling::div[@class="accordion__panel"]/p']

    button_order_middle = [By.CSS_SELECTOR, '.Button_Button__ra12g.Button_Middle__1CSJM']