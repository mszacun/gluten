from  selenium.webdriver.remote import webelement

class WebElement(webelement.WebElement):
    def _find_element(self, by, selector):
        return self.find_element(by, selector)
