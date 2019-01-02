from collections import OrderedDict

from selenium.webdriver.common.by import By

from gluten.element_wrappers import DictElementWrapper
from gluten.locators import Locate, LocateMany, dynamic_locate_many
from gluten.utils import StaticKeys
from gluten.webelements.base import WebElement


class RowWebElement(WebElement):
    _name = Locate('th')


class TableWebElement(WebElement):
    columns = LocateMany('thead tr td')
    _rows = LocateMany('tbody tr', webelement_class=RowWebElement, key=lambda row: row._name.text)

    @property
    def rows(self):
        columns_keys = [col.text for col in self.columns]
        return OrderedDict((key, dynamic_locate_many(row, 'td', key=StaticKeys(columns_keys))) for key, row in self._rows.items())

    def __getitem__(self, item):
        return self.rows[item]
