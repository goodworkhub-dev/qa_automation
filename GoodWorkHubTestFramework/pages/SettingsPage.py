import time

from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass


class Settings(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    hub_and_team = (By.XPATH, "//span[text()='Hub and Team']")
    signup_page = (By.XPATH, "//span[text()='Signup Page']")
    website_settings = (By.XPATH, "//span[text()='Website Settings']")
    org_name_field = (By.CSS_SELECTOR, "input[id='name']")
    add_more_teams_button = (By.XPATH, "//span[text()='Add more teams']")
    new_teams_field = (By.XPATH, "//input[@name='project[0].name']")
    last_team_field = (By.XPATH,  "//div[@class='form-group']//input")
    #//input[@class='form-control']
    update_button = (By.XPATH, "//span[text()='Update']")
    add_more_fields_button = (By.XPATH, "//span[text()='Add more fields']")
    label_field = (By.XPATH, "//input[@id='custom-input-0'] ")
    field_type_field = (By.XPATH, " ")
    mission_statement_field = (By.CSS_SELECTOR, "input[id='mission_statement']")
    contact_information_field = (By.CSS_SELECTOR, "input[id='contact_information']")
    website_setting_update_button = (By.XPATH, "//button[text()='Update']")

    def hub_and_team_click(self):
        self.driver.find_element(*Settings.hub_and_team).click()

    def update_org_name(self):
        return self.driver.find_element(*Settings.org_name_field)

    def update(self):
        return self.driver.find_element(*Settings.update_button)

    def add_teams(self, team_name):
        self.driver.find_element(*Settings.add_more_teams_button).click()
        self.driver.find_element(*Settings.new_teams_field).send_keys(team_name)

    def teams_name(self):
        return self.driver.find_elements(*Settings.last_team_field)

    def signup_page_click(self):
        self.driver.find_element(*Settings.signup_page).click()

    def website_settings_click(self):
        self.driver.find_element(*Settings.website_settings).click()

    def mission_statement_update(self, statement):
        self.driver.find_element(*Settings.mission_statement_field).send_keys(statement)

    def contact_information_update(self, contact):
        self.driver.find_element(*Settings.contact_information_field).send_keys(contact)

    def website_setting_update(self):
        return self.driver.find_element(*Settings.website_setting_update_button)