import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def base_url():
    return "https://automationpractice.com/index.php"

@pytest.fixture
def driver(request):
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1920,1080")
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=opts)
    driver.implicitly_wait(5)

    yield driver

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        driver.save_screenshot(f"reports/selenium-{request.node.name}.png")
    driver.quit()

def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
