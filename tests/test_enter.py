#Тестирование Входа
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestEnter:
# Проверь: вход
# вход по кнопке «Войти в аккаунт» на главной
    def test_enter_by_enter_account_button(self, driver):
        driver.find_element(By.XPATH, "//button[contains(@class,'button_button_type_primary')]").click()
        driver.find_element(By.XPATH, "//input[@type='text']").send_keys('ruslanbagautdinov12@yandex.ru')
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys('123456')
        driver.find_element(By.XPATH, "//button[contains(@class,'button_button_type_primary')]").click()
        assert WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Оформить заказ')]"))).text == 'Оформить заказ'

# вход через кнопку «Личный кабинет»
    def test_enter_by_personal_account_button(self, driver):
        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        driver.find_element(By.XPATH, "//input[@type='text']").send_keys('ruslanbagautdinov12@yandex.ru')
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys('123456')
        driver.find_element(By.XPATH, "//button[contains(@class,'button_button_type_primary')]").click()
        assert WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Оформить заказ')]"))).text == 'Оформить заказ'


# вход через кнопку в форме регистрации
    def test_enter_by_registration_button(self, driver):
        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        driver.find_element(By.XPATH, "//a[contains(text(),'Зарегистрироваться')]").click()
        driver.find_element(By.XPATH, "//a[contains(text(),'Войти')]").click()
        driver.find_element(By.XPATH, "//input[@type='text']").send_keys('ruslanbagautdinov12@yandex.ru')
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys('123456')
        driver.find_element(By.XPATH, "//button[contains(@class,'button_button_type_primary')]").click()
        assert WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Оформить заказ')]"))).text == 'Оформить заказ'

# вход через кнопку в форме восстановления пароля
    def test_enter_by_password_recovery_button(self, driver):
        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        driver.find_element(By.XPATH, "//a[contains(text(),'Восстановить пароль')]").click()
        driver.find_element(By.XPATH, "//a[contains(text(),'Войти')]").click()
        driver.find_element(By.XPATH, "//input[@type='text']").send_keys('ruslanbagautdinov12@yandex.ru')
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys('123456')
        driver.find_element(By.XPATH, "//button[contains(@class,'button_button_type_primary')]").click()
        assert WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Оформить заказ')]"))).text == 'Оформить заказ'

