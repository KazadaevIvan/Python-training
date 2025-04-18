"""
This module contains shared fixtures.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: '--browser_name=chrome' or '--browser_name=firefox'")

    parser.addoption('--language', action='store', default=None,
                     help="Choose language: '--language=en' or '--language=ru'")

@pytest.fixture
def browser(request):
    service = Service("drivers/chromedriver.exe")
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(service=service, options=options)
    browser.implicitly_wait(10)
    browser.maximize_window()

    yield browser

    browser.quit()