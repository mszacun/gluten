import pytest

from selenium import webdriver

@pytest.fixture(scope='session')
def firefox(request):
    driver = webdriver.Firefox()
    yield driver
    driver.close()
