import pytest

from gluten.page import Page
from gluten.locators import Locate

from tests.utils import WebDriverTestCase, get_fixture_url


class SimplePage(Page):
    heading = Locate('h1')
    paragraph = Locate('p')

    def open(self):
        fixture_url = get_fixture_url('test_page_fixture.html')
        self._go_to_url(fixture_url)


class TestPage(WebDriverTestCase):
    @classmethod
    @pytest.fixture(autouse=True, scope='class')
    def setup_class(cls, firefox):
        super(TestPage, cls).setup_class(firefox)
        cls.page = SimplePage(driver=firefox)
        cls.page.open()

    def test_should_allow_to_inject_webdriver_to_page_object(self):
        expected_url = get_fixture_url('test_page_fixture.html')
        assert self.firefox.current_url == expected_url

    def test_should_allow_to_locate_single_element_on_page(self):
        assert self.page.heading.text == 'My First Heading'
        assert self.page.paragraph.text == 'My first paragraph.'
