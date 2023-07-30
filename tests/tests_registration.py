from selenium.webdriver.common.by import By
import re
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Locators:
    LK_BUTTON = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")

# Проверь: Успешную регистрацию.
#Успешную регистрацию. Поле «Имя» должно быть не пустым; в поле Email введён email в формате логин@домен: например, 123@ya.ru. Минимальный пароль — шесть символов.
class TestRegistration:

    def test_registration_correct(self, driver, get_name, get_mail, get_password):
        driver.find_element(*Locators.LK_BUTTON).click()
        driver.find_element(By.XPATH, "//a[contains(@class,'Auth')]").click()
        name = get_name
        driver.find_element(By.XPATH, "(//input[@name='name'])[1]").send_keys(name)
        mail = get_mail
        driver.find_element(By.XPATH, "(//input[@name='name'])[2]").send_keys(mail)
        password = get_password
        driver.find_element(By.CSS_SELECTOR, "input[name='Пароль']").send_keys(password)
        driver.find_element(By.XPATH, "//button[contains(@class,'button_button_type_primary')]").click()
        driver.find_element(*Locators.LK_BUTTON).click()
        driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys(mail)
        driver.find_element(By.CSS_SELECTOR, "input[name='Пароль']").send_keys(password)
        driver.find_element(By.XPATH, "//button[contains(@class,'button_button_type_primary')]").click()
        driver.find_element(*Locators.LK_BUTTON).click()
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        assert WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='Name']"))).get_attribute('value') != '' \
               and re.fullmatch(regex, mail).string == driver.find_element(By.XPATH, f"//input[@value='{mail}']").get_attribute('value')\
               and len(driver.find_element(By.XPATH, "//input[@type='password']").get_attribute('value')) >= 5

    # Ошибку для некорректного пароля.
    def test_registration_password_incorrect(self, driver, get_password):
        driver.find_element(*Locators.LK_BUTTON).click()
        driver.find_element(By.XPATH, "//a[contains(@class,'Auth')]").click()
        driver.find_element(By.CSS_SELECTOR, "input[name='Пароль']").send_keys(get_password[:5])
        driver.find_element(By.XPATH, ".//button").click()
        assert driver.find_element(By.XPATH, ".//p[@class='input__error text_type_main-default']").text == 'Некорректный пароль'
