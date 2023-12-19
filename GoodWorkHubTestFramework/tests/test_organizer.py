"""Test Organizer Features."""
from test_data.login_data import LoginData
from pages.dashboard_page import DashboardPage
from utilities.baseclass import BaseClass
from pages.login_page import Login
import pytest

class TestOrgUserDetails(BaseClass):
    """Test Organizer Features."""

    def test_orgenterdetails(self, get_data):
        """Test Organizer Features."""
        #Login
        login = Login(self.driver)
        login.get_url(get_data['url'])
        login.email_field().send_keys(get_data['email'])
        login.password_field().send_keys(get_data['password'])
        login.submit_button()
        #all organizer elements are found
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
        people_obj = dashboard_obj.people_visible()
        people_obj.peoplelink()
        people_obj.invite_volunteer_click()
        # Messages Features
        messages_obj = dashboard_obj.messages_visible()
        messages_obj.messages_link()
        messages_obj.compose_button_click()
        messages_obj.compose_message('Science','organizer test email')
        messages_obj.delete_message()


    @pytest.fixture(params=LoginData.test_orguser_loginpage_data)
    def get_data(self, request):
        """Use to Login."""
        return request.param
