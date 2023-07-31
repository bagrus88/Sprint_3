from selenium.webdriver.common.by import By
import re
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestRegistration:

    def test_registration_correct(self, driver, wait, get_name, get_mail, get_password):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        name = get_name
        driver.find_element(*Locators.REGISTRATION_INPUT_NAME_BUTTON).send_keys(name)
        mail = get_mail
        driver.find_element(*Locators.REGISTRATION_INPUT_EMAIL_BUTTON).send_keys(mail)
        password = get_password
        driver.find_element(*Locators.REGISTRATION_INPUT_PASSWORD_BUTTON).send_keys(password)
        driver.find_element(*Locators.REGISTRATION_CHECK_BUTTON).click()
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.INPUT_MAIL_BUTTON).send_keys(mail)
        driver.find_element(*Locators.INPUT_PASSWORD_BUTTON).send_keys(password)
        driver.find_element(*Locators.ENTER_BUTTON).click()
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        assert wait.until(EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT_NAME_INFO_BUTTON)).get_attribute('value') != '' \
               and re.fullmatch(regex, mail).string == driver.find_element(By.XPATH, f"//input[@value='{mail}']").get_attribute('value')\
               and len(driver.find_element(*Locators.PERSONAL_ACCOUNT_MAIL_INFO_BUTTON).get_attribute('value')) >= 5

    def test_registration_password_incorrect(self, driver, get_password):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        driver.find_element(*Locators.REGISTRATION_INPUT_PASSWORD_BUTTON).send_keys(get_password[:5])
        driver.find_element(*Locators.REGISTRATION_CHECK_BUTTON).click()
        assert driver.find_element(By.XPATH, ".//p[@class='input__error text_type_main-default']").text == 'Некорректный пароль'
