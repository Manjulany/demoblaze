import os
import json
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import config_reader


# run before running the tests scenarios
def before_scenario(context, driver):

    browser_name = config_reader.read_configuration("basic info", "browser")
    headless_mode = config_reader.read_headless_mode("settings", "headless")

    # call different browser based on given basic info in config file
    if browser_name.__eq__("chrome"):
        # option to run test in headless mode
        chrome_options = Options()
        if headless_mode:
            chrome_options.add_argument("--headless")  # Run in headless mode
        context.driver = webdriver.Chrome(options=chrome_options)
        context.driver.implicitly_wait(30)
    elif browser_name.__eq__("firefox"):
        context.driver = webdriver.Firefox()
    elif browser_name.__eq__("edge"):
        context.driver = webdriver.Edge()

    context.driver.maximize_window()
    context.driver.get(config_reader.read_configuration("basic info", "url"))

    # read data from test data file
    current_file_path = os.path.abspath(__file__)
    current_dir = os.path.dirname(current_file_path)
    project_dir = os.path.dirname(current_dir)

    test_data = os.path.join(project_dir, 'test_data.json')
    with open(test_data, 'r') as file:
        context.data = json.load(file)
        context.add_item = context.data["ADD"]
        context.removal_item = context.data["REMOVE"]


# run after running the tests scenarios
def after_scenario(context, driver):
    context.driver.quit()
