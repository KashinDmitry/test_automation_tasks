from web_automation_task_1.pages.base_search_page import BaseSearchPage
from web_automation_task_1.locators import SearchResultPageLocators


class SearchResultPage(BaseSearchPage):
    def enter_formula_to_calculator(self, formula):
        keys = formula.split()
        for key in keys:
            self.browser.find_element(*SearchResultPageLocators.calculator_buttons[key]).click()

    def show_calculation_result(self):
        show_result_button = SearchResultPageLocators.calculator_buttons["="]
        self.browser.find_element(*show_result_button).click()

    def should_be_entered_formula_in_calculator_memory_field(self, previously_entered_formula):
        memory_field = SearchResultPageLocators.CALCULATOR_MEMORY_FIELD
        text_in_memory_field = self.browser.find_element(*memory_field).text
        assert text_in_memory_field == previously_entered_formula, f"Wrong formula in memory_field." \
                                                                   f"Should be {previously_entered_formula}, got {text_in_memory_field} instead"

    def should_be_correct_calculation_result(self, expected_result):
        result_field = SearchResultPageLocators.CALCULATOR_INPUT_FIELD
        actual_result = self.browser.find_element(*result_field).text
        assert actual_result == expected_result, f"Wrong calculation result. Should be {expected_result}, got {actual_result} instead"