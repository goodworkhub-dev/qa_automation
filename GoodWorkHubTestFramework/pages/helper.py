import time
from selenium.webdriver.common.by import By



class logout:
    def __init__(self,driver):
        self.driver = driver

    def logout(self):
        self.driver.find_element(By.CLASS_NAME, "avatar-content").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Logout']").click()
        time.sleep(2)
        self.driver.close()

