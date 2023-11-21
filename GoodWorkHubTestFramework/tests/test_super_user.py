import time

import pytest

from TestData.LoginData import LoginData
from utilities.BaseClass import BaseClass
from pages.LoginPage import Login


class TestSuperUserDetails(BaseClass):
    def test_superenterdetails(self,getData):
        log = self.getLogger()
        #Login
        login = Login(self.driver)
        login.get_url(getData["url"])
        login.login_button()
        login.email_field().send_keys(getData["email"])
        login.password_field().send_keys(getData["password"])
        dashboard_obj=login.submit_button()
        #all superuser elements are found
        dashboard_obj.dashboard_visible()
        dashboard_obj.donations_visible()
        dashboard_obj.events_visible()
        dashboard_obj.files_visible()
        dashboard_obj.grants_visible()
        dashboard_obj.messages_visible()
        dashboard_obj.people_visible()
        dashboard_obj.planning_visible()
        #People Features
        people_obj =dashboard_obj.people_visible()
        people_obj.People_Link()
        time.sleep(2)
        people_obj.Invite_Volunteer_Click()
        time.sleep(2)

    @pytest.fixture(params=LoginData.test_superuser_loginpage_data)
    def getData(self,request):
        return request.param