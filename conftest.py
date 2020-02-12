import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en")


@pytest.fixture
def lang(request):
    return request.config.getoption("--language")
    
@pytest.fixture 
def browser(lang):
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': lang})
    browser = webdriver.Chrome(options=options)
    yield browser
    time.sleep(5)
    browser.quit()