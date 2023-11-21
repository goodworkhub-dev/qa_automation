import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class People:
    def __init__(self,driver):
        self.driver = driver
        #log = self.getLogger()

    people_link = (By.XPATH,"//span[normalize-space()='People']")
    invite_volunteer_btn=(By.CSS_SELECTOR,"header[class='sc-fzoXzr ZNaUV'] button:nth-child(1)")
    send_invitation_btn= (By.CSS_SELECTOR,"button[type='submit']")
    def People_Link(self):
        self.driver.find_element(*People.people_link).click()

    def Invite_Volunteer_Click(self):
        self.driver.find_element(*People.invite_volunteer_btn).click()
        time.sleep(2)
        try:
            self.driver.find_element(*People.send_invitation_btn).is_displayed()
            print("send invitation button is displayed")
        except NoSuchElementException:
            print("send invitation button not found")



