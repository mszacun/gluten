# Custom WebElements

Custom WebElements allows to describe structure of webelements that have nested children. Those children can be located using `locators` that are used exactly like in Page Object. 

Custom WebElements by default have all attributes and methods that are defined on [Selenium WebElement](https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.remote.webelement) available.

When using locator on custom webelements is search scope is limited to only to this element. That means that even if there are many elements that matches given selector on page (for example `buttons`), when locator from custom element is used, only elements that
matches this selector **inside this custom element** are returned (for example only buttons inside modal window).

::: tip
Nowadays idea of custom webelements plays nicely with idea of **components** in front-end frameworks (for example: React, Vue, Angular). It recommended that custom webelement should be implemented for every non-trivial component in your application
:::

Custom Webelement is ordinary Python class, therefore it can has methods defined that allows to encapsulate logic required to interact with webelement and introduce nice API for consumers.

Additionaly checking state of custom webelement can be done using Python `properties`. If similar proprties are repeated between custom webelements `Predicates` can be used.

## Example

Below example of webelement for single book can be found and then Gluten's custom webelement that describes it with method and property used.

<Book title="Harry Potter and the Philosopher's Stone" author="J. K. Rowling" isbn="0747532699" :availability="true"/>

```python
class BookWebElement(WebElement):
    title = Locate('.title .field-value')
    author = Locate('.author .field-value')
    isbn = Locate('.isbn .field-value')
    availability = Locate('.availability')

    @property
    def is_available(self):
        return self.availability.text == 'AVAILABLE'

    def rent_book(self):
        if not self.is_available:
            raise Exception('Book is not avialable')
        self.availability.click()
```

## Addtional WebElements methods and properties

::: tip
Gluten wraps all located elements in base `gluten.WebElement` class, so those methods and properties are available on each element tat is located using Gluten's locator system, even when `webelement_class` has not been specified.
:::

### exists

This method can be used to check existance of WebElement that locator returns. 

In opposite to default Selenium behaviour, Gluten does not throw exception when element that should be located does not exist, but instead it returns empty element wrapper. 

When calling `exists` method on empty wrapper it return `True` and if wrapper is not empty it returns `False`.

```python
>>> page.some_element.exists()
True # if element if correctly located
False # if element does not exists
```

### classes
This property returns all classes that wrapped webelement has assigned. Classes are returned in form of `list`

```python
>>> page.some_element.classes
['btn', 'btn-primary']
```

### has_class
This method is used to check is webelement has specified class assigned. It returns `True` when class is present on element, otherwise `False` is returned.

```python
>>> page.some_element.has_class('btn')
True
>>> page.some_element.has_class('btn-danger')
False
```

## Action Chains shortcuts

### double_click
This method performs double click on webelement. 

```python
>>> page.some_element.double_click()
```
