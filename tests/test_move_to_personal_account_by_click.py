from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestPersonalAccount:
    def test_move_personal_account_button_by_click(self, driver, wait):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.INPUT_MAIL_BUTTON).send_keys('ruslanbagautdinov12@yandex.ru')
        driver.find_element(*Locators.INPUT_PASSWORD_BUTTON).send_keys('123456')
        driver.find_element(*Locators.ENTER_BUTTON).click()
        wait.until(EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT_BUTTON)).click()
        assert wait.until(EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT_NAME_INFO_BUTTON)).get_attribute('value') == 'Ruslan'\
        and driver.find_element(*Locators.PERSONAL_ACCOUNT_MAIL_INFO_BUTTON).get_attribute('value') == 'ruslanbagautdinov12@yandex.ru'

    def test_move_consructor_from_personal_account_by_constructor_button(self, driver, wait):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.INPUT_MAIL_BUTTON).send_keys('ruslanbagautdinov12@yandex.ru')
        driver.find_element(*Locators.INPUT_PASSWORD_BUTTON).send_keys('123456')
        driver.find_element(*Locators.ENTER_BUTTON).click()
        wait.until(EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT_BUTTON)).click()
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        assert driver.find_element(*Locators.ASSEMBLE_BURGER_TEXT).text == 'Соберите бургер'

    def test_move_consructor_from_personal_account_by_stellar_button(self, driver, wait):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.INPUT_MAIL_BUTTON).send_keys('ruslanbagautdinov12@yandex.ru')
        driver.find_element(*Locators.INPUT_PASSWORD_BUTTON).send_keys('123456')
        driver.find_element(*Locators.ENTER_BUTTON).click()
        wait.until(EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT_BUTTON)).click()
        driver.find_element(*Locators.STELLAR_BURGER_BUTTON).click()
        assert driver.find_element(*Locators.ASSEMBLE_BURGER_TEXT).text == 'Соберите бургер'

    def test_exit_from_personal_account_by_exit_button(self, driver, wait):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.INPUT_MAIL_BUTTON).send_keys('ruslanbagautdinov12@yandex.ru')
        driver.find_element(*Locators.INPUT_PASSWORD_BUTTON).send_keys('123456')
        driver.find_element(*Locators.ENTER_BUTTON).click()
        wait.until(EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(Locators.EXIT_BUTTON)).click()
        assert wait.until(EC.visibility_of_element_located(Locators.INPUT_MAIL_BUTTON)).text == ""



