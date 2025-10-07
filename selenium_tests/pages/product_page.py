from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductPage(BasePage):
    ADD_TO_CART_BUTTON = (By.ID, "add_to_cart")
    PROCEED_TO_CHECKOUT = (By.CSS_SELECTOR, "a[title='Proceed to checkout']")

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)
        self.click(self.PROCEED_TO_CHECKOUT)
