from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.PeoplePage import People
from utilities.BaseClass import BaseClass


class DashboardPage(BaseClass):
    def __init__(self,driver):
        self.driver = driver
        log = self.getLogger()

    dashboard = (By.XPATH,"//span[text()='Dashboard']")
    people = (By.XPATH,"//span[text()='People']")
    messages = (By.XPATH,"//span[text()='Messages']")
    events = (By.XPATH,"//span[text()='Events']")
    planning = (By.XPATH,"//span[text()='Planning']")
    files = (By.XPATH,"//span[text()='Files']")
    donations = (By.XPATH,"//span[normalize-space()='Donations']")
    grants = (By.XPATH,"//span[text()='Grants']")
    hub_setup = (By.XPATH,"//h4[normalize-space()='Hub Setup Checklist']")

    def dashboard_visible(self):
        log = self.getLogger()
        try:
            self.driver.find_element(*DashboardPage.dashboard)
            log.info("Dashboard element found")
        except NoSuchElementException:
            log.info("Dashboard element not found")

    def people_visible(self):
        log = self.getLogger()
        try:
            self.driver.find_element(*DashboardPage.people)
            log.info("People element found")
            page_obj = People(self.driver)
            return page_obj
        except NoSuchElementException:
            log.info("People element not found")


    def messages_visible(self):
        log = self.getLogger()
        try:
            self.driver.find_element(*DashboardPage.messages)
            log.info("Messages element found")
        except NoSuchElementException:
            log.info("Messages element not found")

    def events_visible(self):
        log = self.getLogger()
        try:
            self.driver.find_element(*DashboardPage.events)
            log.info("Events element found")
        except NoSuchElementException:
            log.info("Events element not found")

    def planning_visible(self):
        log = self.getLogger()
        try:
            self.driver.find_element(*DashboardPage.planning)
            log.info("Planning element found")
        except NoSuchElementException:
            log.info("Planning element not found")

    def files_visible(self):
        log = self.getLogger()
        try:
            self.driver.find_element(*DashboardPage.files)
            log.info("Files element found")
        except NoSuchElementException:
            log.info("Files element not found")

    def grants_visible(self):
        log = self.getLogger()
        try:
            self.driver.find_element(*DashboardPage.grants)
            log.info("Grants element found")
        except NoSuchElementException:
            log.info("Grants element not found")

   
    def donations_visible(self):
        log = self.getLogger()
        try:
            self.driver.find_element(*DashboardPage.donations)
            log.info("Donations element found")
        except NoSuchElementException:
            log.info("Donations element not found")

    def hub_setup_visible(self):
        log = self.getLogger()
        try:
            self.driver.find_element(*DashboardPage.hub_setup)
            log.info("hub setup element found")
        except NoSuchElementException:
            log.info("hub setup element not found")








