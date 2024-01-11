"""Test Super User Features."""
import pytest
from test_data.login_data import LoginData
from utilities.baseclass import BaseClass
from pages.login_page import Login


class TestSuperUserDetails(BaseClass):
    """Test Super User Features."""

    def test_superenterdetails(self, get_data):
        """Test Super User Features."""
        self.driver.implicitly_wait(5)
        #Login
        login = Login(self.driver)
        login.get_url(get_data['url'])
        login.email_field().send_keys(get_data['email'])
        login.password_field().send_keys(get_data['password'])
        dashboard=login.submit_button()
        dashboard.planning_visible()
        #Planning Features
        planning = dashboard.planning_visible()
        planning.planninglink()
        planning.checklistbutton()
        planning.create_checklist('Intro','Maths')
        #planning.edit_checklist('Introduction')
        planning.delete_checklist()
        planning.create_tasks('Prepare','Neeti S')
        planning.mytasks_update('Prepare Maths Intro')
        planning.mytasks_delete()


    @pytest.fixture(params=LoginData.test_superuser_loginpage_data_staging)
    def get_data(self, request):
        """Use to Login."""
        return request.param

