import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass


class Teams(BaseClass):
    def __init__(self,driver):
        self.driver = driver

    teams_link = (By.XPATH,"//span[normalize-space()='Teams']")
    invite_volunteer_btn=(By.CSS_SELECTOR,"header[class='sc-fzoXzr ZNaUV'] button:nth-child(1)")
    send_invitation_btn= (By.CSS_SELECTOR,"button[type='submit']")
    invite_organizer_btn=(By.XPATH,"//button[normalize-space()='Invite Organizers']")
    close_btn= (By.CSS_SELECTOR,".waves-effect.btn-prev.btn.btn-secondary")
    def teams_Link(self):
        self.driver.find_element(*Teams.teams_link).click()

    def invite_volunteer_click(self):
        log = self.getLogger()
        self.driver.find_element(*Teams.invite_volunteer_btn).click()
        time.sleep(2)
        try:
            self.driver.find_element(*Teams.send_invitation_btn).is_displayed()
            log.info("send invitation button is displayed")
        except NoSuchElementException:
            log.info("send invitation button not found")
        self.driver.find_element(*Teams.close_btn).click()
        time.sleep(2)

    def invite_organizers_click(self):
        log = self.getLogger()
        self.driver.find_element(*Teams.invite_organizer_btn).click()
        time.sleep(2)
        try:
            self.driver.find_element(*Teams.send_invitation_btn).is_displayed()
            log.info("send invitation button is displayed")
        except NoSuchElementException:
            log.info("send invitation button not found")
        self.driver.find_element(*Teams.close_btn).click()
        time.sleep(2)