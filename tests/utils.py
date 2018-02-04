import os

import pytest


def get_fixture_url(fixture_name):
    return 'file://' + os.path.join(os.path.dirname(__file__), 'fixtures', fixture_name)


class WebDriverTestCase(object):
    @classmethod
    @pytest.fixture(autouse=True, scope='class')
    def setup_class(cls, firefox):
        cls.firefox = firefox
