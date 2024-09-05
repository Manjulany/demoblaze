from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    cart = "cartur"
    place_order = "//button[contains(text(), 'Place Order')]"

    def click_on_cart(self):
        self.driver.find_element(By.ID, self.cart).click()

    def verify_product(self, item):
        assert self.driver.find_element(By.XPATH, f"//td[contains(text(), '{item}')]").is_displayed()

    def remove_cart_item(self, item):
        product_delete_btn = self.driver.find_element(By.XPATH, f"//td[contains(text(), '{item}')]/following-sibling::td[2]/a[contains(text(), 'Delete')]")
        self.driver.execute_script("arguments[0].click();", product_delete_btn)
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.place_order)))
        self.driver.refresh()
        try:
            self.driver.find_element(By.XPATH, f"//td[contains(text(), '{item}')]").is_displayed()
        except NoSuchElementException:
            print("Element has been removed")
