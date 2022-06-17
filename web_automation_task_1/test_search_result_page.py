from web_automation_task_1.pages.base_search_page import BaseSearchPage
from web_automation_task_1.pages.search_result_page import SearchResultPage


class TestSearchResultPage():

    def test_find_calculator_and_do_math(self, browser):
        google_search_page = BaseSearchPage(browser)
        search_result_page = SearchResultPage(browser)

        google_search_page.open_search_page()
        google_search_page.enter_search_request_in_search_field('calculator')
        google_search_page.click_search_button()
        search_result_page.enter_formula_to_calculator('1 * 2 - 3 + 1')
        search_result_page.show_calculation_result()
        search_result_page.should_be_entered_formula_in_calculator_memory_field('1 × 2 - 3 + 1 =')
        search_result_page.should_be_correct_calculation_result('0')