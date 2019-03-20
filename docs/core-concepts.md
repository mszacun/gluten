
# Core concepts


## Page Object

Page Object Pattern is centered about Page Object concept. Page Object describes how page is built, what elements does it contain. Additionally it allows to access those elements and interact with them using complex actions.

All Page objects created using Gluten are created by inheriting from `gluten.page.Page` base class. The simplest, empty Page object looks like this:

```python
from gluten import Page


class EmptyPageObject(Page):
    pass
```

To describe structure of page and elements it contains, we use **locators**. Those classes are configured with details that are needed to find and retrive element from page. Every class atribute that you define as locator, can be later used to access page element described by this locator.

::: tip
By default locators use *css selectors* to locate elements on page. All selectors that are supported by Selenium are allowed.
:::

For example if page contains "OK" button with `ok-button` class:

```html
<html>
  <body>
    <button class="ok-button">Ok</button>
  </body>
</html>
```
it would be described with the following code:

```python
from gluten import Page, Locate


class EmptyPageObject(Page):
    ok_button = Locate('.ok-button')
```

After instantiating and navigating to page, you can access and interact with using `ok_button` attribute. It has all
attributes and methods that ordinary Selenium `WebElement` has, for example `text` attribiute and `click` method presented
below.

```python 
>>> empty_page_object.ok_button
<gluten.element_wrappers.FoundElementWrapper object at 0x7f370ab1bbd0> 
>>> empty_page_object.ok_button.text
'Ok'
>>> empty_page_object.ok_button.click()
```

## Custom WebElements

Pages usually have hierarchical stucture. That means it can contain two kind of elements:
  - simple leaf elements that does not have further children, for example `<button/>, <input/>`
  - elements that contain children elements, for example `<div/>, <table/>, <ul/>`

To allow easier interaction with the latter, Gluten allows to define custom webelemnts. Custom webelement can be used to describe structure of element that contains children. 

Custom webelement is defined by inheriting from `gluten.webelements.base.WebElement`

```python
from gluten import WebElement

class EmptyCustomElement(WebElement):
    pass
```

Accessing children elements is possible with locators, exactly the same way as with Page Objects. The main difference is that when locator is used in custom webelement, its search scope is limited to this element, whereas when used in Page Object it searches for webelement inside whole page. 

For example if a book is described with the following element:
<Book title="Harry Potter and the Philosopher's Stone" author="J. K. Rowling" isbn="0747532699" :availability="true"/>

and its source:
```html
<div class="book">
    <div class="description">
        <div class="basic-info">
            <div class="title">
                <span class='field-name'>Title: </span>
                <span class='field-value'>Harry Potter and the Philosopher's Stone</span>
            </div>
            <div class="author">
                <span class="field-name">Author: </span>
                <span class="field-value">J. K. Rowling</span>
            </div>
            <div class="isbn">
                <span class="field-name">ISBN: </span>
                <span class="field-value">0747532699</span>
            </div>
        </div>
        <p class="availability">AVAILABLE</p>
    </div>
</div>
```

It can be described using following custom webelement:

```python
from gluten import Locate, WebElement


class BookWebElement(WebElement):
    title = Locate('.title .field-value')
    author = Locate('.author .field-value')
    isbn = Locate('.isbn .field-value')
    availability = Locate('.availability')
```

This webelement can be used in Page Object to describe page structure. To let locator know, that located element is described by custom webelement class, we use `webelement_class` argument of locator class. When later accessing page attribute, locator automatically converts retrived webelement to specified webelement class.

```python
from gluten import Page, Locate


class BookPage(Page):
    book = Locate('.book', webelement_class=BookWebElement)
```

When webelement is used inside Page Object it can be used to access this element, and then access its children:

```python
>>> books_page.book.title.text
"Harry Potter and the Philosopher's Stone"
>>> books_page.book.author.text
'J. K. Rowling'
>>> books_page.book.isbn.text
'0747532699'
```

::: tip
This is powerfull feature, that allows to use easier and more understable selectors to describe pages. Additionaly it allows for composing pages of custom webelements and reusing them between different pages. 
:::

Nesting of custom webelements is also possible, so custom components can contain other custom components. Using this pattern leads to more readable code that deals with pages.

```python
from gluten import Page, Locate, WebElement


class BookFieldWebElement(WebElement):
    name = Locate('.field-name')
    value = Locate('.field-value')


class BookWebElement(WebElement):
    title = Locate('.title', webelement_class=BookFieldWebElement)
    author = Locate('.author', webelement_class=BookFieldWebElement)
    isbn = Locate('.isbn', webelement_class=BookFieldWebElement)


class BookPage(Page):
    book = Locate('.book', webelement_class=BookWebElement)


>>> books_page.book.title.name.text
'Title: '
>>> books_page.book.title.value.text
"Harry Potter and the Philosopher's Stone"
>>> books_page.book.author.name.text
'Author: '
>>> books_page.book.title.value.text
'J. K. Rowling'
```

This example presents two important concepts:
1. Similar page elements can be described with single webelement class. Here `BookFieldWebElement` is used to describe all fields of book. Using this webelement we can access both field name and field value separately, without using dirty string parsing or other tricks. Similary if there would be multiple books listed on page, `BookWebElement` could be used to describe all of them.
2. Each webelement has its own search scope. Thanks to this feature, `books_page.book.title` (that locates `<div/>` with "title" class) is accessed, and then `value` attribute is retrived, title's field value is returned. This leads to exactly the same effect as using more complicated selector in previous example (`.title .field-value`), but when custom webelement is used, additionaly `field-name` can be accessed.
