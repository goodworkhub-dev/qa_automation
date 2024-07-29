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
    teams = (By.XPATH, "//span[text()='Teams']")
    messages = (By.XPATH, "//span[text()='Messages']")
    events = (By.XPATH, "//span[text()='Events']")
    todolist = (By.XPATH, "//span[text()='ToDo Lists']")
    files = (By.XPATH, "//span[text()='Files']")
    donations = (By.XPATH, "//span[normalize-space()='Donations']")
    grants = (By.XPATH, "//span[text()='Grants']")
    settings = (By.XPATH, "//span[text()='Settings']")
    switch_hub_tab = (By.XPATH, "//span[text()='Switch Hub']")
    user_avatar = (By.XPATH, "//div[class ='avatar bg-danger avatar-md'] span[class ='avatar-content']")
    sign_out_button = (By.XPATH, "//div[@role='menu']//a[@role='menuitem']")
    create_new_hub_tab= (By.XPATH, "//button[@role='menuitem']")
    grants_tile = (By.XPATH, "(//div[@class='card-body'])[1]")
    teams_tile = (By.XPATH, "(//div[@class='card-body'])[2]")
    volunteers_tile = (By.XPATH, "(//div[@class='card-body'])[3]")
    events_tile = (By.XPATH, "(//div[@class='card-body'])[4]")
    files_tile = (By.XPATH, "(//div[@class='card-body'])[5]")
    help_icon = (By.XPATH, "//*[@title='Click for Help'])")
    hub_todos_tiles = (By.XPATH, "//div[@class='card-additional-title card-header'])[1]")
    quick_links_tiles = (By.XPATH, "//div[@class='card-header']")



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

    def verify_grants_tile(self):
        return self.driver.find_element(*DashboardPage.grants_tile)

    def verify_teams_tile(self):
        return self.driver.find_element(*DashboardPage.teams_tile)

    def verify_volunteers_tile(self):
        return self.driver.find_element(*DashboardPage.volunteers_tile)

    def verify_events_tile(self):
        return self.driver.find_element(*DashboardPage.events_tile)

    def verify_files_tile(self):
        return self.driver.find_element(*DashboardPage.files_tile)

    def verify_help_icon(self):
        return self.driver.find_element(*DashboardPage.help_icon)

    def verify_hub_todos_tiles(self):
        return self.driver.find_element(*DashboardPage.hub_todos_tiles)

    def verify_quick_links_tiles(self):
        return self.driver.find_element(*DashboardPage.quick_links_tiles)

