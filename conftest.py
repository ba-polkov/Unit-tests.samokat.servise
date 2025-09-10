import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from urls import BASE_URL

@pytest.fixture (scope = 'function')
def driver():
    firefox_options = Options()
    driver = webdriver.Firefox(options = firefox_options)
    driver.get (BASE_URL)
    yield driver
    driver.quit()