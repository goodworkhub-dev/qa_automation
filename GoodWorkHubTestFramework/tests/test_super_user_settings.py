import time
import pytest
import os

from utilities.BaseClass import BaseClass
from pages.LoginPage import Login
from TestData.LoginData import LoginData
from pages.SettingsPage import Settings


class TestSuperUserSettings(BaseClass):

    def test_superuser_settings(self, getData):
        # Login
        login = Login(self.driver)
        # login.get_url(getData["url"])
        # login.login_button()
        login.get_url("https://app.goodworkhub.com/login")
        time.sleep(15)
        login.email_field().send_keys(getData["email"])
        time.sleep(5)
        login.password_field().send_keys(getData["password"])
        time.sleep(5)
        login.login_button()
        time.sleep(20)
        dashboard_obj = login.org_select()
        time.sleep(10)
        dashboard_obj.settings_visible().click()
        time.sleep(40)

    # def test_superuser_org_update(self):
    #     settings_obj = Settings(self.driver)
    #     settings_obj.update_org_name().send_keys("EducationForAll_Update")
    #     settings_obj.update().click()

    # def test_add_more_teams(self):
    #     settings_obj = Settings(self.driver)
    #     # settings_obj.add_teams("testnewteam")
    #     # settings_obj.update().click()
    #     ls = settings_obj.teams_name()
    #     for l in ls:
    #         print(l.get_attribute('value'))
        # for l in ls:
        #     if l.get_attribute('value').equals("testnewteam"):
        #         print("MATCH")
        #     else:
        #         print("NOT MATCH")
    #   assert val == "testnewteam"
    # verify the input value

    def test_signup_page_add_more_fields(self):
        settings_obj = Settings(self.driver)
        settings_obj.signup_page_click()

        time.sleep(15)
    #     # verify signup form
    #
    # def test_website_settings(self):
    #     settings_obj = Settings(self.driver)
    #     settings_obj.website_settings_click()
    #     time.sleep(15)
    #     settings_obj.mission_statement_update("test mission")
    #     settings_obj.contact_information_update("test contact")
    #     settings_obj.website_setting_update().click()


    @pytest.fixture(params=LoginData.test_superuser_loginpage_data)
    def getData(self, request):
        return request.param
