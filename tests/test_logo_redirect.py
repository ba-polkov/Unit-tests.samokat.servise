import allure
import pytest
from page.main_page import MainPage
from config import PageTitle
from locators.main_page_locators import MainPageLocators

class TestLogoRedirect:
    
    @allure.title('Переход на главную страницу сервиса при клике на лого "Самокат" в шапке')
    def test_logo_redirect_to_main_page_success(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visability_of_order_button_in_header()
        main_page.click_on_order_button_in_header()
        main_page.wait_visability_of_header_logo_scooter()
        main_page.click_on_header_logo_scooter()
        main_page.wait_visability_of_main_header()
        
        assert main_page.check_displaying_of_main_header        
    
    
    @allure.title('Переход на страницу "Дзена" при клике на лого "Яндекс" в шапке')
    def test_logo_redirect_to_dzen_success(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visability_of_header_logo_yandex()
        main_page.click_on_header_logo_yandex()
        main_page.switch_to_next_tab()
        
        assert main_page.get_page_title() == PageTitle.YANDEX_TITLE