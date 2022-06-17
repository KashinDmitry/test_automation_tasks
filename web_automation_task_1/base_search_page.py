from .locators import BaseSearchPageLocators


class BaseSearchPage():
    def __init__(self, browser, timeout=5):
        self.browser = browser
        self.google_url = 'http://google.com'
        self.browser.implicitly_wait(timeout)

    def open_search_page(self):
        self.browser.get(self.google_url)

    def enter_search_request_in_search_field(self, text_to_search):
        search_field = BaseSearchPageLocators.GOOGLE_SEARCH_FIELD
        self.browser.find_element(*search_field).send_keys(text_to_search)

    def click_search_button(self):
        search_button = BaseSearchPageLocators.GOOGLE_SEARCH_BUTTON
        self.browser.find_element(*search_button).click()

    def get_text(self, element):
        text = self.browser.find_element(*element).text
        return text

