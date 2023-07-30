import random
import string
import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    browser = webdriver.Chrome()
    browser.get('https://stellarburgers.nomoreparties.site')
    browser.maximize_window()
    yield browser
    browser.quit()

@pytest.fixture()
def get_name():
    name = ''.join(random.choice(string.ascii_uppercase) for _ in range(6))
    return name

@pytest.fixture()
def get_mail():
    mail = ''.join(random.choice(string.ascii_lowercase) for _ in range(10)) + '@yandex.ru'
    return mail

@pytest.fixture()
def get_password():
    password = ''.join(random.choice(string.ascii_letters) for _ in range(6))
    return password
