import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.helper import logout


@pytest.fixture(scope="class")
def org_setup(request):
    browser_name=request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    #driver.get("https://educationforall.goodworkhub.com/signin")
    driver.get("https://goodworkhub.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    logout(driver)

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
        )


