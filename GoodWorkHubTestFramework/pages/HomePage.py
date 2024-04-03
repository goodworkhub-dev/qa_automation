from selenium.webdriver.common.by import By
import time
from pages.LoginPage import Login
from pages.SignupPage import SignupPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver


    sign_up = (By.XPATH, "//a[normalize-space()='Sign Up']")
    login = (By.XPATH, "// a[normalize-space() = 'Login']")

    def get_home_page(self):
        self.driver.get("https://goodworkhub.com/")

    # def click_home(self, url):
    #     self.driver.find_element(*HomePage.home).click()
    #     home_obj = HomePage(self.driver)
    #     return home_obj

    def click_sign_up(self):
        self.driver.find_element(*HomePage.sign_up).click()
        signup_obj = SignupPage(self.driver)
        return signup_obj

    def click_login(self):
        self.driver.find_element(*HomePage.login).click()
        login_obj = Login(self.driver)
        return login_obj

    def switch_window(self):
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)


    def close_window(self):
        self.driver.close()