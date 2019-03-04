import pytest

from tests.pages.table_with_replaced_elements_page import TableWithReplacedElementsPage
from tests.utils import WebDriverTestCase


class TestTableWebElement(WebDriverTestCase):
    @classmethod
    @pytest.fixture(autouse=True, scope='class')
    def setup_class(cls, firefox):
        super(TestTableWebElement, cls).setup_class(firefox)
        cls.page = TableWithReplacedElementsPage(driver=cls.firefox)
        cls.page.open()

    def test_should_allow_using_methods_from_overriden_cell_webelement(self):
        assert self.page.table['MEM_MONITORING']['302'].is_marked_as_my_team
        assert self.page.table['MEM_MONITORING']['303'].is_marked_as_my_team
        assert self.page.table['PIT']['305'].is_marked_as_my_team

        assert not self.page.table['PIT']['306'].is_marked_as_my_team
        assert not self.page.table['ALIGNMENTS']['299'].is_marked_as_my_team

    def test_should_allow_changing_column_header_webelement_and_using_methods(self):
        assert self.page.table.columns_headers['300'].is_marked_as_current_sprint
        assert not self.page.table.columns_headers['299'].is_marked_as_current_sprint

    def test_should_allow_changing_row_webelement_and_using_methods(self):
        assert self.page.table.rows['TOGGLERS'].is_marked_selected
        assert not self.page.table.rows['CI_CORE'].is_marked_selected

    def test_should_allow_chaning_row_header_webelement_and_using_methods(self):
        assert self.page.table.rows_headers['ALIGNMENTS'].is_prioritized
        assert not self.page.table.rows_headers['PIT'].is_prioritized

    def test_should_allow_changing_header_and_customizing_the_way_label_is_obtained(self):
        reversed_rows_headers = ['STNEMNGILA', 'EROC_IC', 'GNIROTINOM_MEM', 'TIP', 'SRELGGOT']
        reversed_columns_headers = [
            '992', '003', '103', '203', '303', '403', '503', '603', '703', '803', '903', '013', '113', '213', '313'
        ]

        assert self.page.table_with_reversed_headers.rows_headers.keys() == reversed_rows_headers
        assert self.page.table_with_reversed_headers.columns_headers.keys() == reversed_columns_headers
