from selenium.webdriver.common.by import By
from sendApplicationForm.Pages.locators import locators

class AuthorizationPage:

    def __init__(self, driver):
        self.driver = driver

        self.login_field_id = locators.login_field_id
        self.login_page_button_id = locators.login_page_button_id
        self.pswrd_field_id = locators.pswrd_field_id

    def enter_login(self, login):
        self.driver.find_element(By.ID, self.login_field_id).send_keys(login)
        self.driver.find_element(By.ID, self.login_page_button_id).click()

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.pswrd_field_id).send_keys(password)
        self.driver.find_element(By.ID, self.login_page_button_id).click()
