import time
import pytest
from selenium.webdriver.common.by import By

from pages.RegisteredOrgUser_Login import orguser_login



#Enter supeuser login details
@pytest.mark.usefixtures("org_setup")
class TestOrgUserDetails():
    def test_orgenterdetails(self):
        op = orguser_login(self.driver)
        # Enter login details
        op.org_user_login("neetis282+09Nov@gmail.com", "Thursday@123")
        # click login button
        op.org_click_submit()
        get_url = self.driver.current_url
        print("The current url is:" + str(get_url))
        assert get_url == "https://educationforall.goodworkhub.com/dashboard"
        # click on people tab
        self.driver.find_element(By.XPATH, "//span[normalize-space()='People']").click()
        get_url_people = self.driver.current_url
        print("The current url is:" + str(get_url_people))
        assert get_url_people == "https://educationforall.goodworkhub.com/members"
        # click on messages tab
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Messages']").click()
        get_url_message = self.driver.current_url
        print("The current url is:" + str(get_url_message))
        assert get_url_message == "https://educationforall.goodworkhub.com/messages"
        # click on Event & Meetings tab
        self.driver.find_element(By.CSS_SELECTOR, ".d-flex.align-items-center[href='/calendar']").click()
        get_url_event = self.driver.current_url
        print("The current url is:" + str(get_url_event))
        assert get_url_event == "https://educationforall.goodworkhub.com/calendar"
        # click on Planning tab
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Planning']").click()
        get_url_plan = self.driver.current_url
        print("The current url is:" + str(get_url_plan))
        assert get_url_plan == "https://educationforall.goodworkhub.com/planning"
        # click on files tab
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Files']").click()
        get_url_files = self.driver.current_url
        print("The current url is:" + str(get_url_files))
        assert get_url_files == "https://educationforall.goodworkhub.com/files"

        # click on donations tab
        self.driver.find_element(By.CSS_SELECTOR, ".d-flex.align-items-center[href='/donations']").click()
        get_url_donations = self.driver.current_url
        print("The current url is:" + str(get_url_donations))
        assert get_url_donations == "https://educationforall.goodworkhub.com/donations"

        # click on Grants tab
        self.driver.find_element(By.CSS_SELECTOR, ".d-flex.align-items-center[href='/grants']").click()
        get_url_grants = self.driver.current_url
        print("The current url is:" + str(get_url_grants))
        assert get_url_grants == "https://educationforall.goodworkhub.com/grants"
        # Logout
        self.driver.find_element(By.CLASS_NAME, "avatar-content").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Logout']").click()
        time.sleep(2)

