from selenium.webdriver.common.by import By
import time

from pages.DashboardPage import DashboardPage


class Login:

    def __init__(self, driver):
        self.driver = driver

    email = (By.ID, "register-email")
    password = (By.ID, "register-password")
    submit = (By.CSS_SELECTOR, "button[type='submit']")
    # login_link = (By.XPATH, "//a[text()='Login']")
    login = (By.XPATH, "//button[text()='Login']")
    org_name = (By.CLASS_NAME, "org-name")

    def get_url(self, url):
        self.driver.get(url)
        time.sleep(2)

    def email_field(self):
        return self.driver.find_element(*Login.email)

    def password_field(self):
        return self.driver.find_element(*Login.password)

    def submit_button(self):
        self.driver.find_element(*Login.submit).click()
        dashboard_obj = DashboardPage(self.driver)
        return dashboard_obj

    def click_login_button(self):
        self.driver.find_element(*Login.login).click()
        # dashboard_obj = DashboardPage(self.driver)
        # return dashboard_obj

    def org_select(self):
        self.driver.find_element(*Login.org_name).click()
        dashboard_obj = DashboardPage(self.driver)
        return dashboard_obj
