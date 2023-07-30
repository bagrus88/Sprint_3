from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Переход в личный кабинет. Проверь переход по клику на «Личный кабинет».
class TestPersonalAccount:
    def test_move_personal_account_button_by_click(self, driver):
        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        driver.find_element(By.XPATH, "//input[@type='text']").send_keys('ruslanbagautdinov12@yandex.ru')
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys('123456')
        driver.find_element(By.XPATH, "//button[contains(@class,'button_button_type_primary')]").click()
        WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Личный Кабинет')]"))).click()
        assert WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='Name']"))).get_attribute('value') == 'Ruslan'\
        and driver.find_element(By.XPATH, "//input[@value='ruslanbagautdinov12@yandex.ru']").get_attribute('value') == 'ruslanbagautdinov12@yandex.ru'

#Переход из личного кабинета в конструктор. Проверь переход по клику на «Конструктор»
    def test_move_consructor_from_personal_account_by_constructor_button(self, driver):
        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        driver.find_element(By.XPATH, "//input[@type='text']").send_keys('ruslanbagautdinov12@yandex.ru')
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys('123456')
        driver.find_element(By.XPATH, "//button[contains(@class,'button_button_type_primary')]").click()
        WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Личный Кабинет')]"))).click()
        driver.find_element(By.XPATH, "//p[contains(text(),'Конструктор')]").click()
        assert driver.find_element(By.XPATH, "//h1[contains(text(),'Соберите бургер')]").text == 'Соберите бургер'


#Переход из личного кабинета в конструктор.  Проверь переход по кликуна логотип Stellar Burgers.
    def test_move_consructor_from_personal_account_by_stellar_button(self, driver):
        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        driver.find_element(By.XPATH, "//input[@type='text']").send_keys('ruslanbagautdinov12@yandex.ru')
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys('123456')
        driver.find_element(By.XPATH, "//button[contains(@class,'button_button_type_primary')]").click()
        WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Личный Кабинет')]"))).click()
        driver.find_element(By.XPATH, "//header/nav[1]/div[1]/a[1]/*[1]").click()
        assert driver.find_element(By.XPATH, "//h1[contains(text(),'Соберите бургер')]").text == 'Соберите бургер'


#Выход из аккаунта. Проверь выход по кнопке «Выйти» в личном кабинете.
    def test_exit_from_personal_account_by_exit_button(self, driver):
        driver.maximize_window()
        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        driver.find_element(By.XPATH, "//input[@type='text']").send_keys('ruslanbagautdinov12@yandex.ru')
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys('123456')
        driver.find_element(By.XPATH, "//button[contains(@class,'button_button_type_primary')]").click()
        WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Личный Кабинет')]"))).click()
        WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(@class,'Account')]"))).click()
        assert WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, "//h2"))).text == "Вход"



