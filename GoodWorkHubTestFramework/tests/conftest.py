import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://goodworkhub.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

@pytest.fixture(scope="class")
def org_setup(request):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://educationforall.goodworkhub.com/signin")
        driver.maximize_window()
        request.cls.driver = driver
        yield
        driver.close()

