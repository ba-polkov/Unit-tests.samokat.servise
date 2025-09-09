import allure
from locators.order_page_locators import OrderPageLocators
from page.base_page import BasePage
from data import TestData

class OrderPage(BasePage):
    
    @allure.step ('Клик по списку станций Метро в селекте')
    def select_station(self):
        self.click_on_element(OrderPageLocators.select_item_in_metro)
    
    @allure.step ('Ввод даты в поле ввода')
    def send_keys_date_by_keyboard_input(self):
        self.send_keys_to_input(OrderPageLocators.input_date).send_keys(TestData.test_data_user_1[5])
    
    @allure.step ('Клик по выбранной дате в выпадающем окне Календарь поля даты начала аренды')
    def click_date_on_calendar(self):
        self.click_on_element(OrderPageLocators.calendar_item)
    
    @allure.step ('Отображение кнопки "Посмотреть статус" после создания заказа')
    def check_displaying_of_button_check_status_of_order(self):
        return self.check_displaying_of_element(OrderPageLocators.button_check_status_of_order)
    
    @allure.step ('Заполнение первой формы и нажатие кнопки Далее')
    def data_entry_first_form(self,test_data):
        self.wait_visability_of_elements(OrderPageLocators.input_name)
        self.click_on_element(OrderPageLocators.input_name)
        self.send_keys_to_input(OrderPageLocators.input_name, test_data[0])
        self.click_on_element(OrderPageLocators.input_last_name)
        self.send_keys_to_input(OrderPageLocators.input_last_name, test_data[1])
        self.click_on_element(OrderPageLocators.input_adress)
        self.send_keys_to_input(OrderPageLocators.input_adress, test_data[2])
        self.click_on_element(OrderPageLocators.input_metro)
        self.send_keys_to_input(OrderPageLocators.input_metro, test_data[3])
        self.click_on_element(OrderPageLocators.select_item_in_metro)
        self.click_on_element(OrderPageLocators.input_phone)
        self.send_keys_to_input(OrderPageLocators.input_phone, test_data[4])
        self.click_on_element(OrderPageLocators.button_next)
    
    @allure.step ('Заполнение второй формы и окно подтвержднения')
    def data_entry_second_form(self, test_data):
        self.wait_visability_of_elements(OrderPageLocators.input_date)
        self.click_on_element(OrderPageLocators.input_date)
        self.send_keys_to_input(OrderPageLocators.input_date, test_data[5])
        self.click_on_element(OrderPageLocators.check_box_grey_collor_scooter)
        self.click_on_element(OrderPageLocators.field_rental_period)
        self.click_on_element(OrderPageLocators.dropdown_rental_period)
        self.click_on_element(OrderPageLocators.input_comment)
        self.send_keys_to_input(OrderPageLocators.input_comment, test_data[6])
        self.click_on_element(OrderPageLocators.button_make_order)
        self.wait_visability_of_elements(OrderPageLocators.button_yes_confirm_order)
        self.click_on_element(OrderPageLocators.button_yes_confirm_order)