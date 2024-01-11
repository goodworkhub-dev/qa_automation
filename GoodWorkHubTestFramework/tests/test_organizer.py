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
        dashboard = DashboardPage(self.driver)
        dashboard.dashboard_visible()
        dashboard.donations_visible()
        dashboard.events_visible()
        dashboard.files_visible()
        dashboard.grants_visible()
        dashboard.messages_visible()
        dashboard.people_visible()
        dashboard.planning_visible()
        # People Features
        people_obj = dashboard.people_visible()
        people_obj.peoplelink()
        people_obj.invite_volunteer_click()
        # Messages Features
        messages = dashboard.messages_visible()
        messages.messages_link()
        messages.compose_button_click()
        messages.compose_message('Science','organizer test email')
        messages.delete_message()


    @pytest.fixture(params=LoginData.test_orguser_loginpage_data)
    def get_data(self, request):
        """Use to Login."""
        return request.param
