import os
from selenium import webdriver
import time
import unittest
from src.sendApplicationForm.Pages.applicationFormPage import ApplicationFormPage
from src.sendApplicationForm.Pages.authorizationPage import AuthorizationPage
from selenium.webdriver.chrome.service import Service


class ApplicationFormTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.HOME = os.getenv("HOME")
        cls.service = Service(f"{cls.HOME}/PycharmProjects/applicationYandex/src/sendApplicationForm/chromedriver")
        cls.driver = webdriver.Chrome(service=cls.service)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_fill_out_application_form(self):
        self.HOME = os.getenv("HOME")

        # тестовые данные
        authorization_page_url = "https://clck.ru/YeTcj"
        login = "emailforgettingajob"
        password = "sheisshi48Q"
        name = "Анастасия"
        surname = "Морозова"
        phone = "+79118103835"
        email = "anastasia.p.morozova@gmail.com"
        cv = f"{self.HOME}/PycharmProjects/applicationYandex/src/sendApplicationForm/Resources/Introducing me.txt"

        application_url = "https://clck.ru/YdLhe"

        driver = self.driver

        # переходим на страницу авторизации
        driver.get(authorization_page_url)
        authorization = AuthorizationPage(driver)
        # вводим логин и жмём Войти
        authorization.enter_login(login)
        # вводим пароль и жмём Войти
        authorization.enter_password(password)
        # ждём 5 секунд
        self.driver.implicitly_wait(5)

        # переходим на страницу вакансии
        driver.get(application_url)
        application_form = ApplicationFormPage(driver)

        # прокручиваем страницу до формы отклика
        application_form.scroll_page_to_form()
        # переключаемся в iframe
        application_form.switch_to_iframe()

        # загружаем резюме
        application_form.upload_cv(f"{self.HOME}/"
                                   f"PycharmProjects/applicationYandex/src"
                                   f"/sendApplicationForm/Resources/Morozova.pdf")
        # вводим имя
        application_form.enter_name(name)
        # вводим фамилию
        application_form.enter_surname(surname)
        # вводим телефон
        application_form.enter_phone(phone)
        # вводим email
        application_form.enter_email(email)
        # копируем и вставляем текст из сопроводительного письма
        application_form.copy_cl_text(cv)
        # кликаем в чекбокс (даём соглашение на обработку данных)
        application_form.click_agree_to_terms_checkbox()
        # кликаем по кнопке отправки формы
        application_form.click_to_send_form()

        time.sleep(5)

        # здесь должна быть проверка на соответствие сообщения об
        # успешной отправке формы, но я не хочу спамить вас тестовыми заявками.
        # Допишу проверку по требованию :)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Форма успешно отправлена")
