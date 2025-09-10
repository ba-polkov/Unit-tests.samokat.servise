import allure
from locators.main_page_locators import MainPageLocators
from page.base_page import BasePage

class MainPage(BasePage):
    
    @allure.step ('Ожидание загрузки кнопки Закать в хедере')
    def wait_visability_of_order_button_in_header(self):
        self.wait_visibility_of_element(MainPageLocators.order_button_in_header)
    
    @allure.step ('Клик по кнопке Заказать в хедере')
    def click_on_order_button_in_header(self):
        self.click_on_element(MainPageLocators.order_button_in_header)
    
    @allure.step ('Ожидание загрузки "Самокат" (лого) в хедере')
    def wait_visability_of_header_logo_scooter(self):
        self.wait_visibility_of_element(MainPageLocators.header_logo_scooter)
    
    @allure.step ('Ожидание загрузки "Яндекс" (лого) в хедере')
    def wait_visability_of_header_logo_yandex(self):
        self.wait_visibility_of_element(MainPageLocators.header_logo_yandex)
    
    @allure.step ('Клик по лого "Самокат" в хедере')
    def click_on_header_logo_scooter(self):
        self.click_on_element(MainPageLocators.header_logo_scooter)
    
    @allure.step ('Клик по лого "Яндекс" в хедере')
    def click_on_header_logo_yandex(self):
        self.click_on_element(MainPageLocators.header_logo_yandex)
        
    @allure.step ('Ожидание отображаения заголовка главной страницы')
    def wait_visability_of_main_header(self):
        self.wait_visibility_of_element(MainPageLocators.main_header)
    
    @allure.step ('Отображение заголовка главной страницы')
    def check_displaying_of_main_header(self):
        return self.check_displaying_of_element(MainPageLocators.main_header)
    
    @allure.step ('Скролл до "Вопросы о важном"')
    def scroll_to_faq_section(self):
        self.scroll_to_element(MainPageLocators.faq_section)
    
    @allure.step ('Прогрузка нужного вопроса в "Вопросы о важном"')
    def wait_visability_of_faq_items(self,data):
        self.wait_visibility_of_element(MainPageLocators.faq_question_items[data])
    
    @allure.step ('Клик по нужному вопросу в "Вопросы о важном')
    def click_on_faq_items(self, data):
        self.click_on_element(MainPageLocators.faq_question_items[data])
    
    @allure.step ('Прогрузка ответа в "Вопросы о важном"')
    def wait_visability_of_faq_answer(self, data):
        self.wait_visibility_of_element(MainPageLocators.faq_answers_items[data])
    
    @allure.step ('Получение текста ответа в "Вопросы о важном"')
    def get_displayed_text_from_faq_answer (self, data):
        return self.get_text_on_element(MainPageLocators.faq_answers_items[data])