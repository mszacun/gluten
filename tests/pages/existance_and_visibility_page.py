from gluten.locators import Locate
from gluten.page import Page

from tests.utils import get_fixture_url


class ExistanceAndVisibilityPage(Page):
    make_not_visible_button = Locate('#make-not-visible-button')
    make_not_displayed_button = Locate('#make-not-displayed-button')
    remove_button = Locate('#remove-button')

    to_not_be_visible_element = Locate('#to-be-not-visible')
    to_not_be_displayed = Locate('#to-be-not-displayed')
    to_be_removed = Locate('#to-be-removed')

    def open(self):
        fixture_url = get_fixture_url('test_web_element_existance_and_visibility_fixture.html')
        self._go_to_url(fixture_url)
