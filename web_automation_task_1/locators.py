from selenium.webdriver.common.by import By


class BaseSearchPageLocators():
    GOOGLE_SEARCH_FIELD = (By.NAME, "q")
    GOOGLE_SEARCH_BUTTON = (By.NAME, "btnK")


class SearchResultPageLocators():
    CALCULATOR_INPUT_FIELD = (By.CSS_SELECTOR, "[jsname='zLiRgc']")
    CALCULATOR_MEMORY_FIELD = (By.CLASS_NAME, "vUGUtc")
    CALCULATOR_SHOW_RESULT_BUTTON = (By.CSS_SELECTOR, '[jsname="Pt8tGc"]')

    calculator_buttons = {'1': (By.CSS_SELECTOR, '[jsname="N10B9"]'),
                          '2': (By.CSS_SELECTOR, '[jsname="lVjWed"]'),
                          '3': (By.CSS_SELECTOR, '[jsname="KN1kY"]'),
                          '-': (By.CSS_SELECTOR, '[jsname="pPHzQc"]'),
                          '+': (By.CSS_SELECTOR, '[jsname="XSr6wc"]'),
                          '*': (By.CSS_SELECTOR, '[jsname="YovRWb"]'),
                          '=': (By.CSS_SELECTOR, '[jsname="Pt8tGc"]')}