from selenium.webdriver.common.by import By

from gluten.page import Page
from gluten.locators import Locate

from tests.utils import get_fixture_url


class WebElementInteractionPage(Page):
    copied_text = Locate('copied-text', By.ID)
    copy_button = Locate('copy-text', By.ID)
    source_input = Locate('text-input', By.ID)

    counter = Locate('counter', By.ID)
    increment_button = Locate('increment', By.ID)

    remove_div_button = Locate('remove-div-button', By.ID)
    removed_div = Locate('removed-div', By.ID)

    dynamic_classes_div = Locate('dynamic-classes-div', By.ID)
    add_class_button = Locate('add-class-button', By.ID)

    double_click_text_changing_div = Locate('double-click-text-changing-div', By.ID)
    hover_text_changing_div = Locate('hover-text-chainging-div', By.ID)

    def open(self):
        fixture_url = get_fixture_url('test_web_elements_interaction_fixture.html')
        self._go_to_url(fixture_url)
