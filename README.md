# qa_automation
# Prerequisite

## Step 1:Install Python:

download python(depending on your system) from below link:
https://www.python.org/downloads/

Latest version is python 3

## Step 2:Install Pycharm IDE:

download Pycharm IDE from below link:

https://www.jetbrains.com/pycharm/download/?section=mac

## Step 3:Create a new project in pycharm:

To create a project, do one of the following:
Go to File | New Project
On the Welcome screen, click New Project
In the New Project dialog, specify the project name and its location. The dialog may differ depending on the PyCharm edition.
Community
Professional

Next, choose whether you want to create a new environment or use an existing interpreter, by clicking the corresponding radio-button.

Create a main.py welcome script: keep this option selected if you want PyCharm to add the main.py file to your project. This file contains a very simple Python code sample and can be a starting point of your project.

## Step 4:Install selenium with python

Use pip to install the selenium package.
pip install selenium

## Step 5: Install selenium in pycharm

Click “File”, then “Settings”. 
In the Setting window choose your Project and click on “Project Interpreter”. 
After that click on “plus” icon on the right, type “selenium” into the search field. 
Choose “selenium” from the results list and click “Install Package” button. Wait until the package is installed, you’ll see a message when it’s ready.

## Step 6:Install pytest within pycharm

1. Click “File”, then “Settings”.
2. In the Setting window choose your Project and click on “Project Interpreter”. 
3. After that click on “plus” icon on the right, type “selenium” into the search field. 
4. Choose “pytest” from the results list and click “Install Package” button. Wait until the package is installed, you’ll see a message when it’s ready.

## Automation Test Framework Folder Structure:

### Let's break down the purpose of each folder and file:
* tests/: This folder contains test suites and individual test cases.

* pages/: The pages/ folder holds page object classes that represent different pages or components of the web application.

* utils/: The utils/ folder includes utility modules that provide common functions and resources for tests. This can include modules for test data management, configuration settings, logging, and any other reusable functionalities.

* reports/: This folder is used to store test reports.

* screenshots/:This folder is used to store screenshots.

* drivers/: The drivers/ folder contains the necessary browser drivers, such as chromedriver or geckodriver, required for Selenium to interact with browsers.

* README.md: Include a README file to provide project documentation, installation instructions, prerequisites, and other relevant information for developers or contributors.

* conftest.py: This file is used by pytest to define fixtures, which are functions that provide reusable test resources or set up preconditions for tests. You can define fixtures specific to your project's needs in this file, such as a fixture for initializing the Selenium WebDriver.
