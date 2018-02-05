from gluten.locators import Locate
from gluten.page import Page
from tests.utils import get_fixture_url
from gluten.webelements.table import TableWebElement


class TablePage(Page):
    table = Locate('table', webelement_class=TableWebElement)

    def open(self):
        fixture_url = get_fixture_url('test_table_webelements.html')
        self._go_to_url(fixture_url)
