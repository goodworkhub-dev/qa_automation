import time
import pytest
from selenium.webdriver.common.by import By
from pages.RegisteredSuperUser_Login import superuser_login


#Enter supeuser login details
@pytest.mark.usefixtures("setup")
class TestEnterUserDetails():
    def test_enterdetails(self):
        #launching browser and opening goodworkhub
        # Click on login
        lp = superuser_login(self.driver)
        lp.click_login()
        # Enter login details
        lp.user_login("neetis282@gmail.com","Thursday@123")
        #click login button
        lp.click_submit()
        get_url = self.driver.current_url
        print("The current url is:" + str(get_url))
        assert get_url == "https://app.goodworkhub.com/dashboard"
        #click on people tab
        self.driver.find_element(By.XPATH, "//span[normalize-space()='People']").click()
        get_url_people = self.driver.current_url
        print("The current url is:" + str(get_url_people))
        assert get_url_people == "https://app.goodworkhub.com/members"
        # click on messages tab
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Messages']").click()
        get_url_message = self.driver.current_url
        print("The current url is:" + str(get_url_message))
        assert get_url_message == "https://app.goodworkhub.com/messages"
        # click on Event & Meetings tab
        self.driver.find_element(By.CSS_SELECTOR, ".d-flex.align-items-center[href='/calendar']").click()
        get_url_event = self.driver.current_url
        print("The current url is:" + str(get_url_event))
        assert get_url_event == "https://app.goodworkhub.com/calendar"
        # click on Planning tab
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Planning']").click()
        get_url_plan = self.driver.current_url
        print("The current url is:" + str(get_url_plan))
        assert get_url_plan == "https://app.goodworkhub.com/planning"
        # click on files tab
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Files']").click()
        get_url_files = self.driver.current_url
        print("The current url is:" + str(get_url_files))
        assert get_url_files == "https://app.goodworkhub.com/files"

        # click on donations tab
        self.driver.find_element(By.CSS_SELECTOR, ".d-flex.align-items-center[href='/donations']").click()
        get_url_donations = self.driver.current_url
        print("The current url is:" + str(get_url_donations))
        assert get_url_donations == "https://app.goodworkhub.com/donations"

        # click on Grants tab
        self.driver.find_element(By.CSS_SELECTOR, ".d-flex.align-items-center[href='/grants']").click()
        get_url_grants = self.driver.current_url
        print("The current url is:" + str(get_url_grants))
        assert get_url_grants == "https://app.goodworkhub.com/grants"


        # click on settings tab
        self.driver.find_element(By.CSS_SELECTOR, ".d-flex.align-items-center[href='/settings']").click()
        get_url_settings = self.driver.current_url
        print("The current url is:" + str(get_url_settings))
        assert get_url_settings == "https://app.goodworkhub.com/settings"

        #Logout
        self.driver.find_element(By.CLASS_NAME,"avatar-content").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//span[normalize-space()='Logout']").click()
        time.sleep(2)


