from selenium.webdriver.common.by import By
from selenium_tests.pages.home_page import HomePage

def test_checkout_guest(driver, base_url):
    driver.get(base_url)
    home = HomePage(driver)
    home.search("dress")
    driver.find_element(By.CSS_SELECTOR, ".product_img_link").click()
    driver.find_element(By.ID, "add_to_cart").click()
    driver.find_element(By.CSS_SELECTOR, "a[title='Proceed to checkout']").click()
    driver.find_element(By.CSS_SELECTOR, "a.standard-checkout").click()
    assert "Create an account" in driver.page_source or "authentication" in driver.current_url
