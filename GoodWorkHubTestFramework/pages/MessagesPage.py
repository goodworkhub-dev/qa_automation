from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from utilities.BaseClass import BaseClass
from selenium.webdriver.common.by import By
import time

class Messages(BaseClass):
    def __init__(self,driver):
        self.driver = driver

    messages_tab = (By.CSS_SELECTOR,".d-flex.align-items-center[href='/messages']")
    compose_button = (By.XPATH,"//button[normalize-space()='Compose']")
    to_field = (By.CSS_SELECTOR,".select__value-container.select__value-container--is-multi.css-1hwfws3")
    subject_field = (By.ID,"email-subject")
    send_button = (By.XPATH,"//button[normalize-space()='Send']")

    def messages_link(self):
        self.driver.find_element(*Messages.messages_tab).click()


    def compose_button_click(self):
        self.driver.find_element(*Messages.compose_button).click()
        time.sleep(2)

    def compose_message(self,email):
        to_element = self.driver.find_element(*Messages.to_field)
        action = ActionChains(self.driver)
        action.click(on_element=to_element)
        action.send_keys(email)
        action.key_down(Keys.CONTROL).send_keys(Keys.RETURN).key_up(Keys.CONTROL).perform()
        self.driver.find_element(*Messages.subject_field).send_keys("Test Email")
        self.driver.find_element(*Messages.send_button).click()
        time.sleep(2)




