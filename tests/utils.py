import os

from unittest import TestCase

from selenium import webdriver


def get_fixture_url(fixture_name):
    return 'file://' + os.path.join(os.path.dirname(__file__), 'fixtures', fixture_name)


class WebDriverTestCase(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.close()
