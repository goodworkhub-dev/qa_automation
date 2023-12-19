"""Test Subscriber Features."""
import pytest
from pages.dashboard_page import DashboardPage
from pages.login_page import Login
from test_data.login_data import LoginData
from utilities.baseclass import BaseClass


class TestSubscriberLoginPage(BaseClass):
    """Test Subscriber Features."""

    def test_subscriberenterdetails(self,getData):
        """Test Subscriber Features."""
        # Login
        login = Login(self.driver)
        login.get_url(getData['url'])
        login.email_field().send_keys(getData['email'])
        login.password_field().send_keys(getData['password'])
        login.submit_button()
        # all organizer elements are found
        dashboard_obj = DashboardPage(self.driver)
        dashboard_obj.dashboard_visible()
        dashboard_obj.donations_visible()
        dashboard_obj.events_visible()
        dashboard_obj.messages_visible()
        dashboard_obj.grants_visible()
    # People, Messages, Files, Grants, Settings tabs shouldn’t be visible)   Grants should display or not?
    @pytest.fixture(params=LoginData.test_subscriberuser_loginpage_data)
    def getData(self, request):
        """Use to Login."""
        return request.param

