"""Use for login."""
from selenium.webdriver.common.by import By
import time
from pages.dashboard_page import DashboardPage


class Login:
    """Use for login."""

    def __init__(self,driver):
        """Use to initialize."""
        self.driver = driver

    email = (By.ID, 'register-email')
    password = (By.ID, 'register-password')
    submit = (By.CSS_SELECTOR, "button[type='submit']")
    login_link = (By.LINK_TEXT,'Login')
    def get_url(self,url):
        """Use for url."""
        self.driver.get(url)
        time.sleep(2)
    def email_field(self):
        """Use for email field."""
        return self.driver.find_element(*Login.email)

    def password_field(self):
        """Use for password field."""
        return self.driver.find_element(*Login.password)

    def submit_button(self):
        """Use for submit button."""
        self.driver.find_element(*Login.submit).click()
        time.sleep(2)
        return DashboardPage(self.driver)

    def login_button(self):
        """Use for login button."""
        self.driver.find_element(*Login.login_link).click()
        time.sleep(2)
