from selenium.webdriver.common.by import By
from sendApplicationForm.Pages.locators import locators


class ApplicationFormPage:

    def __init__(self, driver):
        self.driver = driver

        self.upload_CV_button_name = locators.upload_CV_button_name
        self.name_textbox_name = locators.name_textbox_name
        self.surname_textbox_name = locators.surname_textbox_name
        self.phone_textbox_name = locators.phone_textbox_name
        self.email_textbox_name = locators.email_textbox_name
        self.cover_letter_textbox_name = locators.cover_letter_textbox_name
        self.agree_to_terms_checkbox_id = locators.agree_to_terms_checkbox_name
        self.iframe_class_name = locators.iframe_class_name
        self.cookies_button_class = locators.cookies_button_class

    def accept_cookies(self):
        self.driver.find_element(By.CLASS_NAME, self.cookies_button_class)

    def scroll_page_to_form(self):
        flag = self.driver.find_element(By.CLASS_NAME, self.iframe_class_name)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", flag)

    def switch_to_iframe(self):
        iframe = self.driver.find_element(By.CLASS_NAME, self.iframe_class_name)
        self.driver.switch_to.frame(iframe)

    def upload_cv(self, path_to_cv_file):
        self.driver.find_element(By.NAME, self.upload_CV_button_name).send_keys(path_to_cv_file)

    def enter_name(self, name):
        self.driver.find_element(By.NAME, self.name_textbox_name).clear()
        self.driver.find_element(By.NAME, self.name_textbox_name).send_keys(name)

    def enter_surname(self, surname):
        self.driver.find_element(By.NAME, self.surname_textbox_name).clear()
        self.driver.find_element(By.NAME, self.surname_textbox_name).send_keys(surname)

    def enter_phone(self, phone):
        self.driver.find_element(By.NAME, self.phone_textbox_name).clear()
        self.driver.find_element(By.NAME, self.phone_textbox_name).send_keys(phone)

    def enter_email(self, email):
        self.driver.find_element(By.NAME, self.email_textbox_name).clear()
        self.driver.find_element(By.NAME, self.email_textbox_name).send_keys(email)

    def copy_cl_text(self, path_to_cl):
        with open(path_to_cl, 'r') as file:
            cover_letter = file.read()
        self.driver.find_element(By.NAME, self.cover_letter_textbox_name).clear()
        self.driver.find_element(By.NAME, self.cover_letter_textbox_name).send_keys(cover_letter)

    def click_agree_to_terms_checkbox(self):
        self.driver.find_element(By.NAME, self.agree_to_terms_checkbox_id).click()

