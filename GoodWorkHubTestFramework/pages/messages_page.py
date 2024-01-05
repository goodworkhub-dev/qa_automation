"""Use to test Messages Features."""
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from utilities.baseclass import BaseClass
from selenium.webdriver.common.by import By
import time

class Messages(BaseClass):
    """Use to test Messages Features."""

    def __init__(self,driver):
        """Use to initialize."""
        self.driver = driver

    messages_tab = (By.CSS_SELECTOR,".d-flex.align-items-center[href='/messages']")
    compose_button = (By.XPATH,"//button[normalize-space()='Compose']")
    to_field = (By.CSS_SELECTOR,'.select__value-container.select__value-container--is-multi.css-1hwfws3')
    subject_field = (By.ID,'email-subject')
    send_button = (By.XPATH,"//button[normalize-space()='Send']")
    sent_link = (By.XPATH,"//span[text()='Sent']")
    mail_list = (By.XPATH,"//div[@class='mail-details']/div/h5")
    delete_icon = (By.XPATH,"//div[@class='app-content content overflow-hidden email-application']//li[5]//span[1]//*[name()='svg']")

    def messages_link(self):
        """Use to click on messages link."""
        self.driver.find_element(*Messages.messages_tab).click()


    def compose_button_click(self):
        """Use to click on compose button."""
        self.driver.find_element(*Messages.compose_button).click()
        time.sleep(2)

    def compose_message(self,email,subject):
        """Use to click on compose."""
        to_element = self.driver.find_element(*Messages.to_field)
        action = ActionChains(self.driver)
        action.click(on_element=to_element)
        action.send_keys(email)
        action.key_down(Keys.CONTROL).send_keys(Keys.RETURN).key_up(Keys.CONTROL).perform()
        self.driver.find_element(*Messages.subject_field).send_keys(subject)
        self.driver.find_element(*Messages.send_button).click()
        time.sleep(4)

    def delete_message(self):
        """Use to click on delete button."""
        self.driver.find_element(*Messages.sent_link).click()
        self.driver.find_element(*Messages.mail_list).click()
        self.driver.find_element(*Messages.delete_icon).click()







