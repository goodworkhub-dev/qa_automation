import time
import pytest


from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass
from pages.HomePage import HomePage
from pages.LoginPage import Login
from TestData.LoginData import LoginData
from pages.SignupPage import SignupPage

class TestUserHomePage(BaseClass):


    def test_user_login(self, getData):
        # Login
        home = HomePage(self.driver)
        home.get_home_page()
        login = home.click_login()
        home.switch_window()
        # home.close_window()
        login.email_field().send_keys(getData["email"])
        login.password_field().send_keys(getData["password"])
        login.click_login_button()
        time.sleep(10)
        dashboard_obj = login.org_select()
        time.sleep(10)
        dashboard_obj.click_switch_hub().click()
        time.sleep(3)
        dashboard_obj.click_create_new_hub().click()
        # ele = dashboard_obj.click_create_new_hub()
        # if ele.is_displayed():
        #     print("111111")
        time.sleep(3)


    def test_user_signup(self):
        home = HomePage(self.driver)
        home.get_home_page()
        signup_obj = home.click_sign_up()
        home.switch_window()
        ele = signup_obj.get_sign_up_title()
        if ele.is_displayed():
            print("111111")
        time.sleep(3)
        home.close_window()


    @pytest.fixture(params=LoginData.test_superuser_loginpage_data)
    def getData(self, request):
        return request.param

