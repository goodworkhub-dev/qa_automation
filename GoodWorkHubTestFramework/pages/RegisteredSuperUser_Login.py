import time

from selenium.webdriver.common.by import By


class superuser_login:
    def __init__(self,driver):
        self.driver = driver

    def click_login(self):
        self.driver.find_element(By.XPATH,
                                 "//nav[@class='light__DesktopNavLinks-sc-lj69nl-12 light___StyledDesktopNavLinks-sc-lj69nl-13 ghnKnh cDMWyG']//a[@class='light__NavLink-sc-lj69nl-2 light___StyledNavLink-sc-lj69nl-3 ljgxcr liTeQJ'][normalize-space()='Login']").click()
        time.sleep(2)


    def user_login(self,email,password):
        self.driver.find_element(By.ID, "register-email").send_keys(email)
        self.driver.find_element(By.ID, "register-password").send_keys(password)
        time.sleep(2)

    def click_submit(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)