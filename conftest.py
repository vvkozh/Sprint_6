import pytest
import curls
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(curls.url_main_pages)
    yield driver
    driver.quit()