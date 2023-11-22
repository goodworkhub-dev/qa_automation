import time
from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    submitButton = (By.CSS_SELECTOR, "button[type='submit']")
    email = (By.ID, "register-email")
    password= (By.ID, "register-password")
    LoginTab=(By.LINK_TEXT, "Login")

    def clickLogin(self):
        self.driver.find_element(*LoginPage.LoginTab).click()
        time.sleep(2)
    def enterCredentials(self,email,password):
        self.driver.find_element(*LoginPage.email).send_keys(email)
        self.driver.find_element(*LoginPage.password).send_keys(password)
        time.sleep(2)

    def loginSubmit(self):
        self.driver.find_element(*LoginPage.submitButton).click()
        time.sleep(2)




