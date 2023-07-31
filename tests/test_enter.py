from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestEnter:

    def test_enter_by_enter_account_button(self, driver, wait):
        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.INPUT_MAIL_BUTTON).send_keys('ruslanbagautdinov12@yandex.ru')
        driver.find_element(*Locators.INPUT_PASSWORD_BUTTON).send_keys('123456')
        driver.find_element(*Locators.ENTER_BUTTON).click()
        assert wait.until(EC.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON)).text == 'Оформить заказ'

    def test_enter_by_personal_account_button(self, driver, wait):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.INPUT_MAIL_BUTTON).send_keys('ruslanbagautdinov12@yandex.ru')
        driver.find_element(*Locators.INPUT_PASSWORD_BUTTON).send_keys('123456')
        driver.find_element(*Locators.ENTER_BUTTON).click()
        assert wait.until(EC.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON)).text == 'Оформить заказ'

    def test_enter_by_registration_button(self, driver, wait):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        driver.find_element(*Locators.ENTER_FROM_REGISTRATION_BUTTON).click()
        driver.find_element(*Locators.INPUT_MAIL_BUTTON).send_keys('ruslanbagautdinov12@yandex.ru')
        driver.find_element(*Locators.INPUT_PASSWORD_BUTTON).send_keys('123456')
        driver.find_element(*Locators.ENTER_BUTTON).click()
        assert wait.until(EC.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON)).text == 'Оформить заказ'

    def test_enter_by_password_recovery_button(self, driver, wait):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.PASSWORD_RECOVERY_BUTTON).click()
        driver.find_element(*Locators.ENTER_FROM_REGISTRATION_BUTTON).click()
        driver.find_element(*Locators.INPUT_MAIL_BUTTON).send_keys('ruslanbagautdinov12@yandex.ru')
        driver.find_element(*Locators.INPUT_PASSWORD_BUTTON).send_keys('123456')
        driver.find_element(*Locators.ENTER_BUTTON).click()
        assert wait.until(EC.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON)).text == 'Оформить заказ'

