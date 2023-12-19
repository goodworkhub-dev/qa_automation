"""Test Organizer Features."""
from test_data.login_data import LoginData
from pages.dashboard_page import DashboardPage
from utilities.baseclass import BaseClass
from pages.login_page import Login
import pytest

class TestOrgUserDetails(BaseClass):
    """Test Organizer Features."""

    def test_orgenterdetails(self,getData):
        """Test Organizer Features."""
        #Login
        login = Login(self.driver)
        login.get_url(getData['url'])
        login.email_field().send_keys(getData['email'])
        login.password_field().send_keys(getData['password'])
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
        messages_obj.compose_message('Science')
        messages_obj.delete_message()


    @pytest.fixture(params=LoginData.test_orguser_loginpage_data)
    def getData(self, request):
        """Use to Login."""
        return request.param
