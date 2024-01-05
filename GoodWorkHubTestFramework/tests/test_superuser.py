"""Test Super User Features."""
import pytest
from test_data.login_data import LoginData
from utilities.baseclass import BaseClass
from pages.login_page import Login


class TestSuperUserDetails(BaseClass):
    """Test Super User Features."""

    def test_superenterdetails(self, get_data):
        """Test Super User Features."""
        #Login
        login = Login(self.driver)
        login.get_url(get_data['url'])
        login.login_button()
        login.email_field().send_keys(get_data['email'])
        login.password_field().send_keys(get_data['password'])
        dashboard = login.submit_button()
        #all superuser elements are found
        dashboard.dashboard_visible()
        dashboard.donations_visible()
        dashboard.events_visible()
        dashboard.files_visible()
        dashboard.grants_visible()
        dashboard.messages_visible()
        dashboard.people_visible()
        dashboard.planning_visible()
        #Hub Setup visible
        dashboard.hub_setup_visible()
        #People Features
        people = dashboard.people_visible()
        people.peoplelink()
        people.invite_volunteer_click()
        people.invite_organizers_click()
        #Messages Features
        messages = dashboard.messages_visible()
        messages.messages_link()
        messages.compose_button_click()
        messages.compose_message('EducationForAll','super user test email')
        messages.delete_message()
        #Events Features
        events = dashboard.events_visible()
        events.events_link()
        events.event_btn()
        #events_obj.add_event('Intro','EducationForAll','Office')




    @pytest.fixture(params=LoginData.test_superuser_loginpage_data)
    def get_data(self, request):
        """Use to Login."""
        return request.param
