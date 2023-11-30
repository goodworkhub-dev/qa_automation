import pytest
from selenium.webdriver.common.by import By

from pages.LoginPage import LoginPage
from utilities.BaseClass import BaseClass
from pages.DashboardPage import DashboardPage


@pytest.mark.usefixtures("subdomain_setup")
class TestVolunteerLoginPage(BaseClass):

    def testLogin(self,getData):

        loginpage= LoginPage(self.driver)
        loginpage.enterCredentials(getData["email"], getData["password"])
        loginpage.loginSubmit()


        self.verifyLinkPresence("//span[normalize-space()='People']")
        self.verifyLinkPresence("//span[normalize-space()='Messages']")
        self.verifyLinkPresence("//span[normalize-space()='Events']")
        self.verifyLinkPresence("//span[normalize-space()='Planning']")
        self.verifyLinkPresence("//span[normalize-space()='Files']")
        self.verifyLinkPresence("//span[normalize-space()='Donations']")
        self.verifyLinkPresence("//span[normalize-space()='Grants']")


        dashboard = DashboardPage(self.driver)
        self.driver.find_element(*dashboard.peopleTab).click()




    @pytest.fixture(params=[{"email":"yawen@goodworkhub.com","password":"qawyw123"}])
    def getData(self, request):
        return request.param

