import pytest
from selenium import webdriver
from urls import Urls as url

@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def driver_main_page(driver):
    driver.get(url.URL_MAIN)
    yield driver

@pytest.fixture(scope="function")
def driver_order_page(driver):
    driver.get(url.URL_ORDER)
    yield driver
