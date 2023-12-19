"""Use to test People Features."""
import time
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from utilities.baseclass import BaseClass

class People(BaseClass):
    """Use to define people features."""

    def __init__(self,driver):
        """Use to initialize class."""
        self.driver = driver


    people_link = (By.XPATH,"//span[normalize-space()='People']")
    invite_volunteer_btn=(By.CSS_SELECTOR,"header[class='sc-fzoXzr ZNaUV'] button:nth-child(1)")
    send_invitation_btn= (By.CSS_SELECTOR,"button[type='submit']")
    invite_organizer_btn=(By.XPATH,"//button[normalize-space()='Invite Organizers']")
    close_btn= (By.CSS_SELECTOR,'.waves-effect.btn-prev.btn.btn-secondary')
    def peoplelink(self):
        """Use to click on people link."""
        self.driver.find_element(*People.people_link).click()

    def invite_volunteer_click(self):
        """Use to click on invite volunteer button."""
        log = self.get_logger()
        self.driver.find_element(*People.invite_volunteer_btn).click()
        time.sleep(2)
        try:
            self.driver.find_element(*People.send_invitation_btn).is_displayed()
            log.info('send invitation button is displayed')
        except NoSuchElementException:
            log.info('send invitation button not found')
        self.driver.find_element(*People.close_btn).click()
        time.sleep(2)

    def invite_organizers_click(self):
        """Use to click on invite organizers button."""
        log = self.get_logger()
        self.driver.find_element(*People.invite_organizer_btn).click()
        time.sleep(2)
        try:
            self.driver.find_element(*People.send_invitation_btn).is_displayed()
            log.info('send invitation button is displayed')
        except NoSuchElementException:
            log.info('send invitation button not found')
        self.driver.find_element(*People.close_btn).click()
        time.sleep(2)
