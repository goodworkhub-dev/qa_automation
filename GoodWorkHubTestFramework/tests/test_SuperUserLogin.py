import time

import pytest
from selenium.webdriver.common.by import By


from GoodWorkHubTestFramework.pages.RegisteredSuperUser_Login import superuser_login

#launch "goodworkhub" url
'''
class LaunchSite():
    def launchsite(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://goodworkhub.com/")
        driver.maximize_window()
        time.sleep(2)

launchurl = LaunchSite()
launchurl.launchsite()
'''
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



        #Logout
        self.driver.find_element(By.CLASS_NAME,"avatar-content").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//span[normalize-space()='Logout']").click()
        time.sleep(2)


#detailsobj = TestEnterUserDetails()
#detailsobj.test_enterdetails()

#hit enter
#Dashboard should open
#Logout