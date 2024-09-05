from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignupPage:

    def __init__(self, driver):
        self.driver = driver

    signup = "signin2"
    username =  "sign-username"
    password = "sign-password"
    submit = "//button[contains(text(),'Sign up')]"

    def click_on_signup(self):
        self.driver.find_element(By.ID, self.signup).click()

    def enter_singup_credential(self):
        self.driver.find_element(By.ID, self.username).send_keys("testdemouser101")
        self.driver.find_element(By.ID, self.password).send_keys("testdemouser101")

    def click_signup_submit(self):
        self.driver.find_element(By.XPATH, self.submit).click()

    def verify_alert(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()
