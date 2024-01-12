import time

from TestData.LoginData import LoginData
from pages.DashboardPage import DashboardPage
from utilities.BaseClass import BaseClass
from pages.LoginPage import Login
import pytest

class TestVolunteerLoginPage(BaseClass):
    def test_volunteerenterdetails(self,getData):
        # Login
        login = Login(self.driver)
        login.get_url(getData["url"])
        login.email_field().send_keys(getData["email"])
        login.password_field().send_keys(getData["password"])
        dashboard_obj = login.submit_button()
        # all organizer elements are found

        dashboard_obj.dashboard_visible()
        dashboard_obj.donations_visible()
        dashboard_obj.events_visible()
        dashboard_obj.files_visible()
        dashboard_obj.grants_visible()
        dashboard_obj.messages_visible()
        dashboard_obj.people_visible()
        dashboard_obj.planning_visible()
        # People Features
        people_obj = dashboard_obj.people_visible()
        people_obj.People_Link()
        time.sleep(2)
        people_obj.Invite_Volunteer_Click()
        time.sleep(2)
        # Messages Features
        messages_obj = dashboard_obj.messages_visible()
        time.sleep(10)
        messages_obj.messages_link()
        time.sleep(10)
        messages_obj.compose_button_click()
        time.sleep(20)
        messages_obj.compose_message("English Division", "org test email")
        time.sleep(20)
        messages_obj.sent_link()
        time.sleep(20)

    @pytest.fixture(params=LoginData.test_volunteeruser_loginpage_data)
    def getData(self, request):
        return request.param

