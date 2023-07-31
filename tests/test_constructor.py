from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class TestConstructor:
    def test_drag_and_drop_bread(self, driver, wait):
        driver.find_element(*Locators.FILLING_BUTTON).click()
        driver.find_element(*Locators.BEEF_METEORITE_BUTTON).click()
        assert wait.until(EC.visibility_of_element_located(Locators.BEEF_METEORITE_BUTTON)).text == 'Говяжий метеорит (отбивная)' \
               and driver.find_element(*Locators.DETAILS_OF_INGRIDENTS_BUTTON).text == 'Детали ингредиента'

    def test_drag_and_drop_sauce(self, driver, wait):
        driver.find_element(*Locators.SAUCE_BUTTON).click()
        driver.find_element(*Locators.SAUCE_ANTARIAN_BUTTON).click()
        assert wait.until(EC.visibility_of_element_located(Locators.SAUCE_ANTARIAN_BUTTON)).text == 'Соус с шипами Антарианского плоскоходца' \
               and driver.find_element(*Locators.DETAILS_OF_INGRIDENTS_BUTTON).text == 'Детали ингредиента'

    def test_drag_and_drop_filling(self, driver, wait):
        driver.find_element(*Locators.FILLING_BUTTON).click()
        element = driver.find_element(*Locators.FILLING_CHEEZE_WITH_ASTEROID_MOLD)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        assert wait.until(EC.visibility_of_element_located(Locators.FILLING_CHEEZE_WITH_ASTEROID_MOLD)).text == 'Сыр с астероидной плесенью' \
               and driver.find_element(*Locators.DETAILS_OF_INGRIDENTS_BUTTON).text == 'Детали ингредиента'