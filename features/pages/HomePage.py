from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    # define the pages on demoblaze Home page
    homepage_tab = "//a[contains(text(), 'Home')]"
    greetings = "nameofuser"
    phone_tab =  "//a[contains(text(), 'Phones')]"
    laptop_tab = "//a[contains(text(), 'Laptops')]"
    monitors_tab = "//a[contains(text(), 'Monitors')]"
    next_page_btn = "//button[contains(text(), 'Next')]"

    def click_on_home(self):
        homepage_tab = self.driver.find_element(By.XPATH, self.homepage_tab)
        self.driver.execute_script("arguments[0].click();", homepage_tab)           # click command used to click elements not in view
        assert self.driver.find_element(By.ID, self.greetings)

    def open_phone(self, phone_name):
        phone_tab = self.driver.find_element(By.XPATH, self.phone_tab)
        phone = self.driver.find_element(By.XPATH, f"//a[contains(text(), '{phone_name}')]")
        self.driver.execute_script("arguments[0].click();", phone_tab)
        self.driver.execute_script("arguments[0].click();", phone)

    def open_laptop(self, laptop_name):
        self.driver.find_element(By.XPATH, self.laptop_tab).click()
        # dynamically read the item name from json to construct the xpath to recognize the element
        self.driver.find_element(By.XPATH, f"//a[contains(text(), '{laptop_name}')]").click()

    def open_monitor(self, monitor_name):
        self.driver.find_element(By.XPATH, self.monitors_tab).click()
        self.driver.find_element(By.XPATH, f"//a[contains(text(), '{monitor_name}')]").click()

    def open_item(self, item_name):
        try:
            product = self.driver.find_element(By.XPATH, f"//a[contains(text(), '{item_name}')]")
            self.driver.execute_script("arguments[0].scrollIntoView(); arguments[0].click();", product)
        except NoSuchElementException:
            # self.driver.execute_script("arguments[0].click();", self.next_page_btn)
            self.driver.find_element(By.XPATH, self.next_page_btn).click()
            product = self.driver.find_element(By.XPATH, f"//a[contains(text(), '{item_name}')]")
            self.driver.execute_script("arguments[0].scrollIntoView(); arguments[0].click();", product)
