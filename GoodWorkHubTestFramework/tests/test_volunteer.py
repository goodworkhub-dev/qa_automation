"""Test Volunteer Features."""
from test_data.login_data import LoginData
from pages.dashboard_page import DashboardPage
from utilities.baseclass import BaseClass
from pages.login_page import Login
import pytest

class TestVolunteerLoginPage(BaseClass):
    """Test Volunteer Features."""

    def test_volunteerenterdetails(self, get_data):
        """Test Volunteer Features."""
        # Login
        login = Login(self.driver)
        login.get_url(get_data['url'])
        login.email_field().send_keys(get_data['email'])
        login.password_field().send_keys(get_data['password'])
        login.submit_button()
        # all organizer elements are found
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
        people = dashboard.people_visible()
        people.peoplelink()
        people.invite_volunteer_click()
        # Messages Features
        messages = dashboard.messages_visible()
        messages.messages_link()
        messages.compose_button_click()
        #messages_obj.compose_message('English Division','Volunteer Test Email')

    @pytest.fixture(params=LoginData.test_volunteeruser_loginpage_data)
    def get_data(self, request):
        """Use to Login."""
        return request.param

