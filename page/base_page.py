from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        
    @allure.step('Скролим до элемента')
    def scroll_to_element (self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView()', element)
        
    @allure.step ('Ожидание прогрузки элемента')
    def wait_visability_of_elements (self, locator):
        return WebDriverWait(self.driver, 6).until(expected_conditions.visibility_of_element_located(locator))
    
    @allure.step ('Клик по элементу')
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()
        
    @allure.step('Ввод значений в поле')
    def send_keys_to_input(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)
        
    @allure.step('Ролучение текста на элементе')
    def get_text_on_element(self, locator):
        return self.driver.find_element(*locator).text
    
    @allure.step('Переход на другую вкладку')
    def switch_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        
    @allure.step('Получение заголовка страницы')
    def get_page_title (self):
        WebDriverWait(self.driver, 6).until(expected_conditions.presence_of_element_located(MainPageLocators.title_of_page))
        return self.driver.title
    
    @allure.step('Проверяем отбражение элемнета')
    def check_displaying_of_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()    