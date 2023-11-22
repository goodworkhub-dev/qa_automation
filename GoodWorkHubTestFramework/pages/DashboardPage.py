import time
from selenium.webdriver.common.by import By

class DashboardPage:

    def __init__(self, driver):
        self.driver = driver

    peopleTab = (By.XPATH, "//span[normalize-space()='People']")
    messageTab = (By.XPATH, "//span[normalize-space()='Messages']")
    eventsTab = (By.XPATH, "//span[normalize-space()='Events']")
    planningTab = (By.XPATH, "//span[normalize-space()='Planning']")
    filesTab = (By.XPATH, "//span[normalize-space()='Files']")
    donationTab = (By.XPATH, "// span[normalize - space() = 'Donations']")
    grantsTab = (By.XPATH, "// span[normalize - space() = 'Grants']")
    settingsTab = (By.XPATH, "// span[normalize - space() = 'Settings']")

