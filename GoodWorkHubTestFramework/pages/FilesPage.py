from selenium.webdriver import Keys
from utilities.BaseClass import BaseClass
from selenium.webdriver.common.by import By
import time


class Files(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    files_tab = (By.XPATH,"//span[text()='Files']")
    upload_file_button = (By.XPATH,"//input[@id='attach-email-item']")
    new_folder_button = (By.XPATH,"//button[text()='New Folder']")
    file_name_field = (By.XPATH,"//input[@id='name']")
    create_button = (By.XPATH,"//button[text()='Create']")
    upload_file_place = (By.XPATH,"//div[@class='d-flex flex-wrap mt-2']/div[1]/div[2]/h6[1]/a[1]")

    def files_link(self):
        self.driver.find_element(*Files.files_tab).click()

    def upload_file(self, filepath):
        self.driver.find_element(*Files.upload_file_button).send_keys(filepath)

    def create_new_folder(self, folder_name):
        self.driver.find_element(*Files.new_folder_button).click()
        time.sleep(2)
        self.driver.find_element(*Files.file_name_field).send_keys(folder_name)
        time.sleep(2)
        self.driver.find_element(*Files.create_button).click()

    def verify_upload_file(self):
        return self.driver.find_element(*Files.upload_file_place).text()


