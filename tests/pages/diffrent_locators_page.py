from selenium.webdriver.common.by import By

from gluten.page import Page
from gluten.locators import Locate

from tests.utils import get_fixture_url


class DiffrentLocatorsPage(Page):
    located_by_id = Locate('with_id', By.ID)
    located_by_tag_name = Locate('p', By.TAG_NAME)
    located_by_name = Locate('with_name', By.NAME)
    located_by_link_text = Locate('link text', By.LINK_TEXT)
    located_by_class_name = Locate('with_class_name', By.CLASS_NAME)
    located_by_css_selector = Locate('.with_class_name.and_second_class_name')
    located_by_xpath = Locate('//body/ul/*[2]', By.XPATH)

    def open(self):
        fixture_url = get_fixture_url('test_diffrent_locators.html')
        self._go_to_url(fixture_url)
