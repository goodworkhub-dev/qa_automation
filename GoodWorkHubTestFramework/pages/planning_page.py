"""Use to test Planning Features."""
import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from utilities.baseclass import BaseClass

class Planning(BaseClass):
    """Use to define planning features."""

    def __init__(self,driver):
        """Use to initialize class."""
        self.driver = driver

    planning_link = (By.XPATH,"//span[text()='Planning']")
    checklist_button = (By.XPATH,"//button[text()='Create Checklist']")
    checklist_name = (By.ID,'checklist-name')
    team_selection = (By.CSS_SELECTOR,'.select__value-container.select__value-container--has-value.css-1hwfws3')
    create_button = (By.XPATH,"//button[text()='Create']")
    checklist_link = (By.XPATH,"//span[text()='Checklists']")
    select_checklist = (By.XPATH,"//div[@class='content-right']//li[1]")
    delete_button = (By.ID,'checklist-delete-button')
    edit_button = (By.ID,'checklist-edit-button')
    update_button = (By.XPATH,"//button[text()='Update']")
    create_task = (By.ID,'checklist-plus-button')
    task_name = (By.ID,'task-name')
    due_date_field = (By.ID,'task_due_date')
    due_date = (By.XPATH,"//span[text()='25']")
    select_assignee = (By.ID,'task-assignee')
    create_button = (By.XPATH,"//button[text()='Create']")
    mytasks_link = (By.XPATH,"//a[@href='/planning/mytasks']")
    edit_task = (By.ID,'task-edit-button')
    delete_task = (By.ID,'task-delete-button')

    def planninglink(self):
        """Use to click on planning link."""
        self.driver.find_element(*Planning.planning_link).click()

    def checklistbutton(self):
        """Use to click on checklist button."""
        self.driver.find_element(*Planning.checklist_button).click()

    def create_checklist(self,checklistname,team):
        """Use to create checklist."""
        self.driver.find_element(*Planning.checklist_name).send_keys(checklistname)
        to_element = self.driver.find_element(*Planning.team_selection)
        action = ActionChains(self.driver)
        action.click(on_element=to_element)
        action.send_keys(team)
        action.key_down(Keys.CONTROL).send_keys(Keys.RETURN).key_up(Keys.CONTROL).perform()
        time.sleep(5)
        self.driver.find_element(*Planning.create_button).click()
        time.sleep(5)

    def edit_checklist(self,updated_checklistname):
        """Use to edit checklist."""
        self.driver.find_element(*Planning.select_checklist).click()
        time.sleep(5)
        self.driver.find_element(*Planning.edit_button).click()
        time.sleep(5)
        self.driver.find_element(*Planning.checklist_name).clear()
        self.driver.find_element(*Planning.checklist_name).send_keys(updated_checklistname)
        time.sleep(5)
        self.driver.find_element(*Planning.update_button).click()
        time.sleep(5)

    def delete_checklist(self):
        """Use to delete checklist."""
        self.driver.find_element(*Planning.select_checklist).click()
        time.sleep(5)
        self.driver.find_element(*Planning.delete_button).click()
        time.sleep(5)

    def create_tasks(self,taskname,assignee_name):
        """Use to create task."""
        self.driver.find_element(*Planning.select_checklist).click()
        time.sleep(5)
        self.driver.find_element(*Planning.create_task).click()
        time.sleep(5)
        self.driver.find_element(*Planning.task_name).send_keys(taskname)
        self.driver.find_element(*Planning.due_date_field).click()
        self.driver.find_element(*Planning.due_date).click()
        to_element = self.driver.find_element(*Planning.select_assignee)
        action = ActionChains(self.driver)
        action.click(on_element=to_element)
        action.send_keys(assignee_name)
        action.key_down(Keys.CONTROL).send_keys(Keys.RETURN).key_up(Keys.CONTROL).perform()
        time.sleep(5)
        self.driver.find_element(*Planning.create_button).click()
        time.sleep(5)

    def mytasks_update(self,updatedtask):
        """Use to update task."""
        self.driver.find_element(*Planning.mytasks_link).click()
        time.sleep(5)
        self.driver.find_element(*Planning.edit_task).click()
        time.sleep(5)
        self.driver.find_element(*Planning.task_name).clear()
        self.driver.find_element(*Planning.task_name).send_keys(updatedtask)
        time.sleep(5)
        self.driver.find_element(*Planning.update_button).click()
        time.sleep(5)

    def mytasks_delete(self):
        """Use to delete task."""
        self.driver.find_element(*Planning.mytasks_link).click()
        self.driver.find_element(*Planning.delete_task).click()





