import time

from selenium.webdriver.common.by import By


class orguser_login:
    def __init__(self,driver):
        self.driver = driver

    def org_user_login(self,email,password):
        self.driver.find_element(By.ID, "register-email").send_keys(email)
        self.driver.find_element(By.ID, "register-password").send_keys(password)
        time.sleep(2)

    def org_click_submit(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)