from collections import OrderedDict

from selenium.webdriver.common.by import By

from gluten.element_wrappers import DictElementWrapper
from gluten.locators import Locate, LocateMany, dynamic_locate_many
from gluten.utils import StaticKeys
from gluten.webelements.base import WebElement


class HeaderWebElement(WebElement):
    @property
    def label(self):
        return self.text


class TableWebElement(WebElement):
    cell_webelement = WebElement
    column_header_webelement = HeaderWebElement
    row_webelement = WebElement
    row_header_webelement = HeaderWebElement

    @property
    def all_columns_headers(self):
        return dynamic_locate_many(self, 'thead tr th', webelement_class=self.column_header_webelement)

    @property
    def columns_headers(self):
        return OrderedDict((cell.label, cell) for cell in self.all_columns_headers[1:])

    @property
    def rows_headers(self):
        return dynamic_locate_many(self, 'tbody tr th',
                                   key=lambda row: row.label, webelement_class=self.row_header_webelement)

    @property
    def rows(self):
        rows = dynamic_locate_many(self, 'tbody tr', webelement_class=self.row_webelement)
        return OrderedDict((label, row) for label, row in zip(self.rows_headers.keys(), rows))

    def __getitem__(self, item):
        columns_keys = self.columns_headers.keys()
        for key, row in self.rows.items():
            if key == item:
                return dynamic_locate_many(row, 'td', key=StaticKeys(columns_keys), webelement_class=self.cell_webelement)
