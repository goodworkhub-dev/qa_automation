from selenium.webdriver.common.by import By
import time

class Login:

    def __init__(self,driver):
        self.driver = driver

    email = (By.ID, "register-email")
    password = (By.ID, "register-password")
    submit = (By.CSS_SELECTOR, "button[type='submit']")
    login_link = (By.XPATH,"//nav[@class='light__DesktopNavLinks-sc-lj69nl-12 light___StyledDesktopNavLinks-sc-lj69nl-13 ghnKnh cDMWyG']//a[@class='light__NavLink-sc-lj69nl-2 light___StyledNavLink-sc-lj69nl-3 ljgxcr liTeQJ'][normalize-space()='Login']")

    def email_field(self):
        return self.driver.find_element(*Login.email)

    def password_field(self):
        return self.driver.find_element(*Login.password)

    def submit_button(self):
        self.driver.find_element(*Login.submit).click()
        time.sleep(2)

    def login_button(self):
        self.driver.find_element(*Login.login_link).click()
        time.sleep(2)