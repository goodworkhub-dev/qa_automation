from selenium.webdriver.common.by import By


class SignupPage:

    def __init__(self, driver):
        self.driver = driver

    sign_up_title = (By.XPATH, "//h2[normalize-space()='Create Your GoodWork Hub Today!']")


    def get_sign_up_title(self):
        return self.driver.find_element(*SignupPage.sign_up_title)
