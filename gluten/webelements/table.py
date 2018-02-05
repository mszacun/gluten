from selenium.webdriver.common.by import By

from gluten.element_wrappers import DictElementWrapper
from gluten.locators import Locate, LocateMany
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
        return {key: DictElementWrapper(elem, 'td', by=By.CSS_SELECTOR, webelement_class=WebElement,
                                        key=StaticKeys(columns_keys)) for key, elem in self._rows.items()}

    def __getitem__(self, item):
        return self.rows[item]
