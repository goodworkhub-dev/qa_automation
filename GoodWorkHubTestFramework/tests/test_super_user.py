from pages.DashboardPage import DashboardPage
from utilities.BaseClass import BaseClass
from pages.LoginPage import Login


class TestSuperUserDetails(BaseClass):
    def test_superenterdetails(self):
        #Login
        login = Login(self.driver)
        login.login_button()
        login.email_field().send_keys("neetis282@gmail.com")
        login.password_field().send_keys("Thursday@123")
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