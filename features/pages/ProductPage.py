from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    add_to_cart = "//a[contains(text(), 'Add to cart')]"

    def add_product_to_cart(self):
        self.driver.find_element(By.XPATH, self.add_to_cart).click()
        WebDriverWait(self.driver, 300).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()
