import pytest

from tests.pages.table_page import TablePage
from tests.utils import WebDriverTestCase


class TestTableWebElement(WebDriverTestCase):
    @classmethod
    @pytest.fixture(autouse=True, scope='class')
    def setup_class(cls, firefox):
        super(TestTableWebElement, cls).setup_class(firefox)
        cls.page = TablePage(driver=cls.firefox)
        cls.page.open()

    def test_should_allow_to_access_cells_with_rows_columns_keys(self):
        assert self.page.table['PIT']['300'].text == 'FTK3'
        assert self.page.table['TOGGLERS']['305'].text == 'FTK56'
        assert self.page.table['MEM_MONITORING']['313'].text == 'FTK7'

    def test_should_be_able_to_access_rows_names(self):
        expected_rows = ['ALIGNMENTS', 'CI_CORE', 'MEM_MONITORING', 'PIT', 'TOGGLERS']
        assert list(self.page.table.rows.keys()) == expected_rows

    def test_should_be_able_to_access_columns(self):
        expected_names = ['299', '300', '301', '302', '303', '304', '305', '306',
                          '307', '308', '309', '310', '311', '312', '313']
        assert list(self.page.table.columns_headers.keys()) == expected_names

    def test_should_access_column_header_by_key(self):
        assert self.page.table.columns_headers['301'].text == '301'
