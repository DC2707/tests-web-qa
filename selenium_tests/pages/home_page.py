from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    SEARCH_INPUT = (By.ID, "search_query_top")
    SEARCH_BTN = (By.NAME, "submit_search")

    def search(self, term):
        self.type(self.SEARCH_INPUT, term)
        self.click(self.SEARCH_BTN)
