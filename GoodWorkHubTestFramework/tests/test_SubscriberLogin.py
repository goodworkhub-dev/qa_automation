from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from pages.LoginPage import LoginPage

from utilities.BaseClass import BaseClass

@pytest.mark.usefixtures("subdomain_setup")
class TestSubscriberLoginPage(BaseClass):

    def testLogin(self,getData):
        loginpage= LoginPage(self.driver)
        loginpage.enterCredentials(getData["email"], getData["password"])
        loginpage.loginSubmit()

        self.verifyLinkPresence("//span[normalize-space()='Messages']")
        self.verifyLinkPresence("//span[normalize-space()='Events']")
        self.verifyLinkPresence("//span[normalize-space()='Donations']")
        self.verifyLinkPresence("//span[normalize-space()='Grants']")
        assert WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH,"//span[normalize-space()='Files']" )))
        assert WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, "//span[normalize-space()='Settings']")))

        assert WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, "//span[normalize-space()='People']")))

    # People, Messages, Files, Grants, Settings tabs shouldn’t be visible)   Grants should display or not?
    @pytest.fixture(params=[{"email":"wangyawen12+suprt@gmail.com","password":"wyw123456"}])
    def getData(self, request):
        return request.param

