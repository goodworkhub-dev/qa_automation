"""Use for dashboard feature."""
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.events_page import Events
from pages.people_page import People
from utilities.baseclass import BaseClass
from pages.messages_page import Messages


class DashboardPage(BaseClass):
    """Use for dashboard feature."""

    def __init__(self,driver):
        """Use to initialize."""
        self.driver = driver


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
        """Use for dashboard link."""
        log = self.get_logger()
        try:
            self.driver.find_element(*DashboardPage.dashboard)
            log.info('Dashboard element found')
        except NoSuchElementException:
            log.info('Dashboard element not found')

    def people_visible(self):
        """Use for people link."""
        log = self.get_logger()
        try:
            self.driver.find_element(*DashboardPage.people)
            log.info('People element found')
            return People(self.driver)
        except NoSuchElementException:
            log.info('People element not found')


    def messages_visible(self):
        """Use for messages link."""
        log = self.get_logger()
        try:
            self.driver.find_element(*DashboardPage.messages)
            log.info('Messages element found')
            return Messages(self.driver)
        except NoSuchElementException:
            log.info('Messages element not found')

    def events_visible(self):
        """Use for events link."""
        log = self.get_logger()
        try:
            self.driver.find_element(*DashboardPage.events)
            log.info('Events element found')
            return Events(self.driver)
        except NoSuchElementException:
            log.info('Events element not found')

    def planning_visible(self):
        """Use for planning link."""
        log = self.get_logger()
        try:
            self.driver.find_element(*DashboardPage.planning)
            log.info('Planning element found')
        except NoSuchElementException:
            log.info('Planning element not found')

    def files_visible(self):
        """Use for files link."""
        log = self.get_logger()
        try:
            self.driver.find_element(*DashboardPage.files)
            log.info('Files element found')
        except NoSuchElementException:
            log.info('Files element not found')

    def grants_visible(self):
        """Use for grants link."""
        log = self.get_logger()
        try:
            self.driver.find_element(*DashboardPage.grants)
            log.info('Grants element found')
        except NoSuchElementException:
            log.info('Grants element not found')

    def donations_visible(self):
        """Use for donations link."""
        log = self.get_logger()
        try:
            self.driver.find_element(*DashboardPage.donations)
            log.info('Donations element found')
        except NoSuchElementException:
            log.info('Donations element not found')

    def hub_setup_visible(self):
        """Use for hub setup link."""
        log = self.get_logger()
        try:
            self.driver.find_element(*DashboardPage.hub_setup)
            log.info('hub setup element found')
        except NoSuchElementException:
            log.info('hub setup element not found')








