class Page(object):
    def __init__(self, driver):
        self.driver = driver

    def _go_to_url(self, url):
        self.driver.get(url)

    def _find_element(self, by, selector):
        return self.driver.find_element(by, selector)

    def _find_elements(self, by, selector):
        return self.driver.find_elements(by, selector)
