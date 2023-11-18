from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class DashboardPage:
    def __init__(self,driver):
        self.driver = driver

    dashboard = (By.XPATH,"//span[text()='Dashboard']")
    people = (By.XPATH,"//span[text()='People']")
    messages = (By.XPATH,"//span[text()='Messages']")
    events = (By.XPATH,"//span[text()='Events']")
    planning = (By.XPATH,"//span[text()='Planning']")
    files = (By.XPATH,"//span[text()='Files']")
    donations = (By.XPATH,"//span[text()='Donations']")
    grants = (By.XPATH,"//span[text()='Grants']")

    def dashboard_visible(self):
        try:
            self.driver.find_element(*DashboardPage.dashboard)
            print("Dashboard element found")
        except NoSuchElementException:
            print("Dashboard element not found")

    def people_visible(self):
        try:
            self.driver.find_element(*DashboardPage.people)
            print("People element found")
        except NoSuchElementException:
            print("People element not found")

    def messages_visible(self):
        try:
            self.driver.find_element(*DashboardPage.messages)
            print("Messages element found")
        except NoSuchElementException:
            print("Messages element not found")

    def events_visible(self):
        try:
            self.driver.find_element(*DashboardPage.events)
            print("Events element found")
        except NoSuchElementException:
            print("Events element not found")

    def planning_visible(self):
        try:
            self.driver.find_element(*DashboardPage.planning)
            print("Planning element found")
        except NoSuchElementException:
            print("Planning element not found")

    def files_visible(self):
        try:
            self.driver.find_element(*DashboardPage.files)
            print("Files element found")
        except NoSuchElementException:
            print("Files element not found")

    def donations_visible(self):
        try:
            self.driver.find_element(*DashboardPage.donations)
            print("Donations element found")
        except NoSuchElementException:
            print("Donations element not found")

    def grants_visible(self):
        try:
            self.driver.find_element(*DashboardPage.grants)
            print("Grants element found")
        except NoSuchElementException:
            print("Grants element not found")





