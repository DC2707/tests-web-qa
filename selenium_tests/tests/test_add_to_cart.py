from selenium.webdriver.common.by import By
from selenium_tests.pages.home_page import HomePage
from selenium_tests.pages.product_page import ProductPage

def test_add_to_cart(driver, base_url):
    driver.get(base_url)
    home = HomePage(driver)
    home.search("dress")
    first_product = driver.find_element(By.CSS_SELECTOR, ".product_img_link")
    first_product.click()
    product = ProductPage(driver)
    product.add_to_cart()
    assert "Product successfully added" in driver.page_source
