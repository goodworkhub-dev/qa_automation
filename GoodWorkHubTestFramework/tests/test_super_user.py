import time
import pytest
import os

from TestData.LoginData import LoginData
from utilities.BaseClass import BaseClass
from pages.LoginPage import Login


class TestSuperUserDetails(BaseClass):
    def test_superenterdetails(self):
        # Login
        login = Login(self.driver)
        login.get_url("https://app.goodworkhub.com/login")
        time.sleep(5)
        login.email_field().send_keys("neeti@goodworkhub.com")
        login.password_field().send_keys("qwerty")

        # login.email_field().send_keys(getData["email"])
        # login.password_field().send_keys(getData["password"])
        login.login_button()
        # all superuser elements are found
        # dashboard_obj.dashboard_visible()
        # dashboard_obj.donations_visible()
        # dashboard_obj.events_visible()
        # dashboard_obj.files_visible()
        # dashboard_obj.grants_visible()
        # dashboard_obj.messages_visible()
        # dashboard_obj.teams_visible()
        # dashboard_obj.todolist_visible()
        # Hub Setup visible
        # dashboard_obj.hub_setup_visible()
        #Teams Features
        # teams_obj =dashboard_obj.teams_visible()
        # teams_obj.teams_Link()
        # time.sleep(2)
        # teams_obj.invite_volunteer_click()
        # time.sleep(2)
        # teams_obj.invite_organizers_click()
        # time.sleep(2)
        # Messages Features
        # messages_obj=dashboard_obj.messages_visible()
        # time.sleep(2)
        # messages_obj.messages_link()
        # time.sleep(2)
        # messages_obj.compose_button_click()
        # time.sleep(2)
        # messages_obj = dashboard_obj.messages_visible()
        # time.sleep(10)
        # messages_obj.messages_link()
        # time.sleep(80)
        # messages_obj.compose_button_click()
        # time.sleep(20)
        # messages_obj.compose_message("EducationForAll", "superuser test email")
        # time.sleep(20)
        # messages_obj.sent_link()
        # Files Features
        files_obj = dashboard_obj.files_visible()
        time.sleep(15)
        files_obj.files_link()
        time.sleep(30)
        file_path = os.path.abspath('../staticfiles/dog.jpeg')
        files_obj.upload_file(file_path)
        time.sleep(15)
        files_obj.create_new_folder("testSuper")
        time.sleep(5)

    @pytest.fixture(params=LoginData.test_superuser_loginpage_data)
    def getData(self, request):
        return request.param
