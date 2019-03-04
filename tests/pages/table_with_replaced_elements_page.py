from gluten.locators import Locate
from gluten.page import Page
from gluten.webelements.table import TableWebElement, HeaderWebElement
from gluten.webelements.base import WebElement

from tests.utils import get_fixture_url


class ColumnHeaderWebElement(HeaderWebElement):
    @property
    def is_marked_as_current_sprint(self):
        return 'current-sprint' in self.classes


class CellWebelement(WebElement):
    @property
    def is_marked_as_my_team(self):
        return 'my-team' in self.classes


class RowWebElement(WebElement):
    @property
    def is_marked_selected(self):
        return self.has_class('selected')


class RowHeaderWebElement(HeaderWebElement):
    @property
    def is_prioritized(self):
        return self.has_class('prioritized')


class ReversedTableHeader(HeaderWebElement):
    @property
    def label(self):
        return ''.join(reversed(self.text))


class TableWithReplacedElements(TableWebElement):
    cell_webelement = CellWebelement
    column_header_webelement = ColumnHeaderWebElement
    row_webelement = RowWebElement
    row_header_webelement = RowHeaderWebElement


class TableWithReversedHeaders(TableWebElement):
    column_header_webelement = ReversedTableHeader
    row_header_webelement = ReversedTableHeader


class TableWithReplacedElementsPage(Page):
    table = Locate('table', webelement_class=TableWithReplacedElements)
    table_with_reversed_headers = Locate('table', webelement_class=TableWithReversedHeaders)

    def open(self):
        fixture_url = get_fixture_url('test_table_webelements.html')
        self._go_to_url(fixture_url)
