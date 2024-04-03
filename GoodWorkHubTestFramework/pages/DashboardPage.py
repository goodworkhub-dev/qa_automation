from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.TeamsPage import Teams
from utilities.BaseClass import BaseClass
from pages.MessagesPage import Messages
from pages.FilesPage import Files
import time

class DashboardPage(BaseClass):
    def __init__(self,driver):
        self.driver = driver


    dashboard = (By.XPATH, "//span[text()='Dashboard']")
    #Teams
    teams = (By.XPATH, "//span[text()='Teams']")
    messages = (By.XPATH, "//span[text()='Messages']")
    events = (By.XPATH, "//span[text()='Events']")
    #todolist
    todolist = (By.XPATH, "//span[text()='ToDo Lists']")
    files = (By.XPATH, "//span[text()='Files']")
    donations = (By.XPATH, "//span[normalize-space()='Donations']")
    grants = (By.XPATH, "//span[text()='Grants']")
    # hub_setup = (By.XPATH,"//h4[normalize-space()='Hub Setup Checklist']")
    settings = (By.XPATH, "//span[text()='Settings']")
    switch_hub_tab = (By.XPATH, "//span[text()='Switch Hub']")
    user_avatar = (By.XPATH, "//div[class ='avatar bg-danger avatar-md'] span[class ='avatar-content']")
    sign_out_button = (By.XPATH, "//div[@role='menu']//a[@role='menuitem']")
    create_new_hub_tab= (By.XPATH, "//button[@role='menuitem']")


    def dashboard_visible(self):
        log = self.getLogger()
        try:
            time.sleep(10)
            self.driver.find_element(*DashboardPage.dashboard)
            log.info("Dashboard element found")
        except NoSuchElementException:
            log.info("Dashboard element not found",)


    def teams_visible(self):
        log = self.getLogger()
        try:
            time.sleep(5)
            self.driver.find_element(*DashboardPage.teams)
            log.info("teams element found")
            page_obj = People(self.driver)
            return page_obj
        except NoSuchElementException:
            log.info("teams element not found")


    def messages_visible(self):
        log = self.getLogger()
        try:
            self.driver.find_element(*DashboardPage.messages)
            log.info("Messages element found")
            messages_obj = Messages(self.driver)
            return messages_obj
        except NoSuchElementException:
            log.info("Messages element not found")

    def events_visible(self):
        log = self.getLogger()
        try:
            self.driver.find_element(*DashboardPage.events)
            log.info("Events element found")
        except NoSuchElementException:
            log.info("Events element not found")

    def todolist_visible(self):
        log = self.getLogger()
        try:
            self.driver.find_element(*DashboardPage.todolist)
            log.info("todolist element found")
        except NoSuchElementException:
            log.info("todolist element not found")

    def files_visible(self):
        log = self.getLogger()
        try:
            self.driver.find_element(*DashboardPage.files)
            log.info("Files element found")
            files_obj = Files(self.driver)
            return files_obj
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

    # def hub_setup_visible(self):
    #     log = self.getLogger()
    #     try:
    #         self.driver.find_element(*DashboardPage.hub_setup)
    #         log.info("hub setup element found")
    #     except NoSuchElementException:
    #         log.info("hub setup element not found")


    def settings_visible(self):
        log = self.getLogger()
        try:
            log.info("settings element found")
            return self.driver.find_element(*DashboardPage.settings)

        except NoSuchElementException:
            log.info("settings element not found")



    def click_switch_hub(self):
            return self.driver.find_element(*DashboardPage.switch_hub_tab)


    def click_create_new_hub(self):
            return self.driver.find_element(*DashboardPage.create_new_hub_tab)


    def click_user_avatar(self):
        self.driver.find_element(*DashboardPage.user_avatar).click

    def click_sign_out_button(self):
        return self.driver.find_element(*DashboardPage.user_avatar)