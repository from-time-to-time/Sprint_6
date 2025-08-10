import pytest
from selenium import webdriver
from config import Config

@pytest.fixture(scope='function')
def driver():
    firefox = webdriver.Firefox()
    firefox.get(Config.URL)
    yield firefox
    firefox.quit()