import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass


class People(BaseClass):
    def __init__(self,driver):
        self.driver = driver

    people_link = (By.XPATH,"//span[normalize-space()='People']")
    invite_volunteer_btn=(By.CSS_SELECTOR,"header[class='sc-fzoXzr ZNaUV'] button:nth-child(1)")
    send_invitation_btn= (By.CSS_SELECTOR,"button[type='submit']")
    invite_organizer_btn=(By.XPATH,"//button[normalize-space()='Invite Organizers']")
    close_btn= (By.CSS_SELECTOR,".waves-effect.btn-prev.btn.btn-secondary")
    def People_Link(self):
        self.driver.find_element(*People.people_link).click()

    def Invite_Volunteer_Click(self):
        log = self.getLogger()
        self.driver.find_element(*People.invite_volunteer_btn).click()
        time.sleep(2)
        try:
            self.driver.find_element(*People.send_invitation_btn).is_displayed()
            log.info("send invitation button is displayed")
        except NoSuchElementException:
            log.info("send invitation button not found")
        self.driver.find_element(*People.close_btn).click()
        time.sleep(2)

    def Invite_Organizers_Click(self):
        log = self.getLogger()
        self.driver.find_element(*People.invite_organizer_btn).click()
        time.sleep(2)
        try:
            self.driver.find_element(*People.send_invitation_btn).is_displayed()
            log.info("send invitation button is displayed")
        except NoSuchElementException:
            log.info("send invitation button not found")
        self.driver.find_element(*People.close_btn).click()
        time.sleep(2)