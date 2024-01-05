"""Use to test Events Features."""
import time
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.baseclass import BaseClass

class Events(BaseClass):
    """Use to define events features."""

    def __init__(self,driver):
        """Use to initialize class."""
        self.driver = driver

    events_tab = (By.XPATH,"//span[text()='Events']")
    add_event_btn = (By.XPATH,"//span[text()='Add Event']")
    add_title = (By.ID,'title')
    select_guest = (By.XPATH,"//div[text()='Select...']")
    add_location = (By.ID,'location')
    add_button = (By.XPATH,"//button[@type='submit']")
    start_date = (By.ID,'startDate')
    end_date = (By.ID,'endDate')
    select_calendar = (By.XPATH,"//div[@class='flatpickr-calendar hasTime animate showTimeInput open arrowTop']")
    start_current_month = (By.XPATH,"//div[@class='flatpickr-calendar hasTime animate showTimeInput open arrowTop']//select[@class='flatpickr-monthDropdown-months']")
    start_current_year = (By.XPATH,"//div[@class='flatpickr-calendar hasTime animate showTimeInput open arrowTop']//input[@aria-label='Year']")



    def events_link(self):
        """Use to click on events link."""
        self.driver.find_element(*Events.events_tab).click()

    def event_btn(self):
        """Use to click on add event button."""
        self.driver.find_element(*Events.add_event_btn).click()

    """
    def add_event(self,title,email,location):
        
        self.driver.find_element(*Events.add_title).send_keys(title)
        guest_list=self.driver.find_element(*Events.select_guest)
        action = ActionChains(self.driver)
        action.click(on_element=guest_list)
        action.send_keys(email)
        action.key_down(Keys.CONTROL).send_keys(Keys.RETURN).key_up(Keys.CONTROL).perform()
        time.sleep(4)
        self.driver.find_element(*Events.start_date).click()
        wait=WebDriverWait(self.driver,5)
        wait.until(expected_conditions.visibility_of_element_located(*Events.select_calendar))
        current_month=self.driver.find_element(*Events.start_current_month).text
        current_year=self.driver.find_element(*Events.start_current_year).text
        while not (current_month.__eq__('January') and current_year.__eq__('2024')):
            self.driver.find_element(By.XPATH,"//div[@class='flatpickr-calendar hasTime animate showTimeInput open arrowTop']//span[@class='flatpickr-next-month']//*[name()='svg']")
            current_month = self.driver.find_element(*Events.start_current_month).text
            current_year = self.driver.find_element(*Events.start_current_year).text
        
        self.driver.find_element(*Events.add_location).send_keys(location)
        self.driver.find_element(*Events.add_button).click()
        
        """







