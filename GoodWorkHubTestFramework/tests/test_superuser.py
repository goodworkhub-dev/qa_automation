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
        #Hub Setup visible
        dashboard_obj.hub_setup_visible()
        #People Features
        people_obj =dashboard_obj.people_visible()
        people_obj.peoplelink()
        people_obj.invite_volunteer_click()
        people_obj.invite_organizers_click()
        #Messages Features
        messages_obj=dashboard_obj.messages_visible()
        messages_obj.messages_link()
        messages_obj.compose_button_click()
        messages_obj.compose_message('EducationForAll','super user test email')
        messages_obj.delete_message()
        #Events Features
        events_obj=dashboard_obj.events_visible()
        events_obj.events_link()
        events_obj.event_btn()
        #events_obj.add_event('Intro','EducationForAll','Office')




    @pytest.fixture(params=LoginData.test_superuser_loginpage_data)
    def get_data(self, request):
        """Use to Login."""
        return request.param
