import time

from TestData.LoginData import LoginData
from pages.DashboardPage import DashboardPage
from utilities.BaseClass import BaseClass
from pages.LoginPage import Login
import pytest


class TestOrgUserDetails(BaseClass):
    def test_orgenterdetails(self, getData):
        # Login
        login = Login(self.driver)
        login.get_url(getData["url"])
        login.email_field().send_keys(getData["email"])
        login.password_field().send_keys(getData["password"])
        login.submit_button()
        # all organizer elements are found
        dashboard_obj = DashboardPage(self.driver)
        dashboard_obj.dashboard_visible()
        dashboard_obj.donations_visible()
        dashboard_obj.events_visible()
        dashboard_obj.files_visible()
        dashboard_obj.grants_visible()
        dashboard_obj.messages_visible()
        dashboard_obj.people_visible()
        dashboard_obj.planning_visible()
        # People Features
        # people_obj = dashboard_obj.people_visible()
        # people_obj.People_Link()
        # time.sleep(20)
        # people_obj.Invite_Volunteer_Click()
        time.sleep(2)
        # Messages Features
        messages_obj = dashboard_obj.messages_visible()
        time.sleep(10)
        messages_obj.messages_link()
        time.sleep(100)
        messages_obj.compose_button_click()
        time.sleep(10)
        messages_obj.compose_message("Science", "org test email")

    @pytest.fixture(params=LoginData.test_orguser_loginpage_data)
    def getData(self, request):
        return request.param
