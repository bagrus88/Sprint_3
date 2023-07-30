#Раздел «Конструктор».
#Проверь, что работают переходы к разделам:
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#«Булки»
class TestConstructor:
    def test_drag_and_drop_bread(self, driver):
        driver.find_element(By.XPATH, "//span[contains(text(),'Начинки')]").click()
        driver.find_element(By.XPATH, "//p[contains(text(),'Говяжий метеорит (отбивная)')]").click()
        assert WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Говяжий метеорит (отбивная)')]"))).text == 'Говяжий метеорит (отбивная)' \
               and driver.find_element(By.XPATH, "//h2[contains(text(), 'Детали')]").text == 'Детали ингредиента'

# «Соусы»
    def test_drag_and_drop_sauce(self, driver):
        driver.find_element(By.XPATH, "//span[contains(text(),'Соусы')]").click()
        driver.find_element(By.XPATH, "//p[contains(text(),'Соус с шипами Антарианского плоскоходца')]").click()
        assert WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Соус с шипами Антарианского плоскоходца')]"))).text == 'Соус с шипами Антарианского плоскоходца' \
               and driver.find_element(By.XPATH, "//h2[contains(text(), 'Детали')]").text == 'Детали ингредиента'

#«Начинки»
    def test_drag_and_drop_filling(self, driver):
        driver.find_element(By.XPATH, "//span[contains(text(),'Начинки')]").click()
        element = driver.find_element(By.XPATH, "//p[contains(text(),'Сыр с астероидной плесенью')]")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        assert WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Сыр с астероидной плесенью')]"))).text == 'Сыр с астероидной плесенью' \
               and driver.find_element(By.XPATH, "//h2[contains(text(), 'Детали')]").text == 'Детали ингредиента'