from selenium_tests.pages.home_page import HomePage

def test_search_valid(driver, base_url):
    driver.get(base_url)
    home = HomePage(driver)
    home.search("dress")
    assert "Search" in driver.title or "dress" in driver.page_source.lower()
