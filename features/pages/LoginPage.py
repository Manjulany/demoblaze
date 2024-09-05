from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    login = "login2"
    username =  "loginusername"
    password = "loginpassword"
    submit = "//button[contains(text(), 'Log in')]"

    def click_on_signup(self):
        self.driver.find_element(By.ID, self.login).click()

    def enter_login_credential(self):
        self.driver.find_element(By.ID, self.username).send_keys("testdemouser101")
        self.driver.find_element(By.ID, self.password).send_keys("testdemouser101")

    def click_login_submit(self):
        self.driver.find_element(By.XPATH, self.submit).click()
