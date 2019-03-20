# Locators
Locators are used to tell gluten how to find children elements inside page/webelement. Usually they are defined as attributes on Page Objects or custom webelement class, and when they are accessed, retrived webelement(s) is returned.

Each locator needs at least following parameters to locate:
* selector - string that identifies located element
* by - information about strategy that is used to locate element, `By.CSS_SELECTOR` is default strategy [(see available options)](https://selenium-python.readthedocs.io/locating-elements.html)
* Webelement class of retrived element, this can be used to change this class to Custom Webelement for elements with nested children, `gluten.webelements.base.WebElement` is used as default

## Locating single element
To locate single element `gluten.locators.Locate` locator is used. It can imported directly from Gluten:
```python
from gluten import Locate
```

Example usage of `Locate` locator (with specifing different weblement classes and locate strategies) is presented below:

```python
from selenium.webdriver.common.by import By

from gluten import Page, Locate, WebElement


class CustomWebElement(WebElement):
    pass


class ExamplePageWithLocate(Page):
    located_by_id = Locate('with_id', By.ID)
    located_by_tag_name = Locate('p', By.TAG_NAME)
    located_by_name = Locate('with_name', By.NAME)
    located_by_link_text = Locate('link text', By.LINK_TEXT)
    located_by_class_name = Locate('with_class_name', By.CLASS_NAME)
    located_by_css_selector = Locate('.with_class_name.and_second_class_name')
    located_by_xpath = Locate('//body/ul/*[2]', By.XPATH)
    located_by_name_with_custom_webelment = Locate('with_name', By.NAME, webelement_class=CustomWebElement)
```
::: tip
For documentation regarding different types of locating strategy, please consult [Selenium docs](https://selenium-python.readthedocs.io/locating-elements.html)
:::

When attributes defined as locators are accessed, locator searches for element, and returns it.

```python
>>> example_page_with_locate.located_by_link_text
<gluten.element_wrappers.FoundElementWrapper object at 0x7f370ab1bbd0> 
```

## Locating multiple elements
It is very common, that similar elements, can be found, or share similar selector, and all of them are the same element, or have similar structure. This is true for lists of elements, control buttons, table rows, etc.

To locate multiple elements using the same selectors `LocateMany` locator is used. When accessing attribute that is defined as `LocateMany` wrapper that can be thought of as list of elements is returned. It can be indexed and length of the list can be calculated using `len` function, just like with ordinary Python list.

For example if page contains the following unordered list:
<ul>
    <li>Harry Potter and the Philosopher's Stone</li>
    <li>The Lord of the Rings: The Fellowship of the Ring</li>
    <li>The Da Vinci Code</li>
</ul>

```html
<ul>
    <li>Harry Potter and the Philosopher's Stone</li>
    <li>The Lord of the Rings: The Fellowship of the Ring</li>
    <li>The Da Vinci Code</li>
</ul>
```

bullet poins can be retrived using `LocateMany` locator

```python
from gluten import Page, LocateMany


class PageWithBulletList(Page):
    bullets = LocateMany('li')
```

`LocateMany` works exactly like Selenium [find_elements_*](https://selenium-python.readthedocs.io/locating-elements.html) methods.

```python
# LocateMany can be indexed to get individual elements
>>> first_bullet = page_with_bullets.bullets[0]
>>> first_bullet.text
"Harry Potter and the Philosopher's Stone"
>>> page_with_bullets.bullets[1].text
'The Lord of the Rings: The Fellowship of the Ring'

# Length of LocateMany can be taken
>>> len(page_with_bullets.bullets)
3
```

### Locating many custom webelements

`LocateMany` locator, just like `Locate` accepts `webelement_class` argument. When it is specified, each element of the list is converted to desired webelement class.

For example if following list of books is given:
<div>
    <Book title="Harry Potter and the Philosopher's Stone" author="J. K. Rowling" isbn="0747532699" :availability="true"/>
    <Book title="The Lord of the Rings: The Fellowship of the Ring" author=" J. R. R. Tolkien" isbn="9789172632936" :availability="true"/>
    <Book title="The Da Vinci Code" author="Dan Brown" isbn="0385504209" :availability="false"/>
</div>

with source:
```html
<div>
   <div class="book">
      <div class="description">
         <div class="basic-info">
            <div class="title"><span class="field-name">Title: </span> <span class="field-value">Harry Potter and the Philosopher's Stone</span></div>
            <div class="author"><span class="field-name">Author: </span> <span class="field-value">J. K. Rowling</span></div>
            <div class="isbn"><span class="field-name">ISBN: </span> <span class="field-value">0747532699</span></div>
         </div>
         <p class="availability">AVAILABLE</p>
      </div>
   </div>
   <div class="book">
      <div class="description">
         <div class="basic-info">
            <div class="title"><span class="field-name">Title: </span> <span class="field-value">The Lord of the Rings: The Fellowship of the Ring</span></div>
            <div class="author"><span class="field-name">Author: </span> <span class="field-value">J. R. R. Tolkien</span></div>
            <div class="isbn"><span class="field-name">ISBN: </span> <span class="field-value">9789172632936</span></div>
         </div>
         <p class="availability">AVAILABLE</p>
      </div>
   </div>
   <div class="book">
      <div class="description">
         <div class="basic-info">
            <div class="title"><span class="field-name">Title: </span> <span class="field-value">The Da Vinci Code</span></div>
            <div class="author"><span class="field-name">Author: </span> <span class="field-value">Dan Brown</span></div>
            <div class="isbn"><span class="field-name">ISBN: </span> <span class="field-value">0385504209</span></div>
         </div>
         <p class="availability not-available">NOT AVAILABLE</p>
      </div>
   </div>
</div>
```

Each book can be described with the follwing custom webelement (the simplest possible):
```python
class BookWebElement(WebElement):
    title = Locate('.title .field-value')
    author = Locate('.author .field-value')
    isbn = Locate('.isbn .field-value')
    availability = Locate('.availability')
```

Later it can be used in page object:
```python
from gluten import Page, LocateMany


class MultipleBooksPage(Page):
    books = LocateMany('.book', webelement_class=BookWebElement)


# each element of books list can be treated like BookWebElement
>>> multiple_books_page.books[0].title.text
"Harry Potter and the Philosopher's Stone"
>>> multiple_books_page.books[1].author.text
'J. R. R. Tolkien'
```

::: tip
As well as `Locate`, `LocateMany` can be also used inside custom webelements. `BookWebElement` could be also written as
```python
class BookWebElement(WebElement):
    fields_values = LocateMany('.field-value')


# then each field value can be retrived as follows
>>> multiple_books_page.books[0].fields_values[0].text # first field of first book (title)
"Harry Potter and the Philosopher's Stone"
>>> multiple_books_page.books[1].fields_values[1].text # second field of second book (author)
'J. R. R. Tolkien'
```

This is presented here only as example, not as recommended recipe.
:::

## Locating multiple elements with key
Normally, to get specific element from `LocateMany`, it is indexed using number, as previously presented. Sometimes, when elements can move around, or some more descriptive indexing is desired it is very usefull to index elements using some text that it contains.

This is possible using `key` argument, that is passed to `LocateMany`. `key` argument should be a single argument function (possibly lambda) that accepts single argument - retrived element and returns descriptive name that will be used as index to get this this element.

When using `key` argument, wrapper returned by `LocateMany` behaves like `dict` instead of `list` when `LocateMany` is used without `key` argument.

Using previous examples, bullet points can be indexed using its text:
```python
from gluten import Page, LocateMany


class PageWithBulletList(Page):
    bullets = LocateMany('li', key=lambda element: element.text)


# now each bullet point can be indexed like this
>>> page_with_bullets.bullets["Harry Potter and the Philosopher's Stone"]
<gluten.webelements.base.WebElement (session="c0ac65d98cc85ff70c841b99b26c6175", element="0.4134242496803109-25")>
>>> page_with_bullets.bullets['The Lord of the Rings: The Fellowship of the Ring'].text
'The Lord of the Rings: The Fellowship of the Ring'
```

This pattern would be much more usefull, when dealing with many `button` elements. Indexing those button by text would allow
to easily click specifing button using its visible text. Using button text instead of index allows for more readable code.

```python
class ExamplePage(Page):
    buttons = LocateMany('button', key=lambda button: button.text)


page.buttons['Ok'].click()
page.buttons['Cancel'].click()
```

It also very usefull when dealing with custom webelements (using books list from `LocateMany` example above):

```python
from gluten import Page, LocateMany


class BookWebElement(WebElement):
    title = Locate('.title .field-value')
    author = Locate('.author .field-value')
    isbn = Locate('.isbn .field-value')
    availability = Locate('.availability')


class BooksIndexedByTitlePage(Page):
    books_by_title = LocateMany('.book', webelement_class=BookWebElement, key=lambda book: book.title.text)


>>> books_page.books_by_title["Harry Potter and the Philosopher's Stone"].author.text
'J. K. Rowling'
>>> books_page.books_by_title['The Da Vinci Code'].availability.text
'NOT AVAILABLE'
```

::: tip
Notice that function passed as `key` argument, receives webelement that is already converted to desired `webelement_class`. That's way it is possible to use `book.title.text` attributes
:::

Wrapper returned by `LocateMany` with `key` argument behaves like Python's `dict`.

```python
>>> books_page.books_by_title.keys() # it preserves DOM element's order
["Harry Potter and the Philosopher's Stone", 'The Lord of the Rings: The Fellowship of the Ring', 'The Da Vinci Code']
>>> 'Twighlight' in books_page.books_by_title, 'The Da Vinci Code' in books_page.books_by_title
False, True

# .items method is also available
for key, element in books_page.books_by_title.items():
    pass
```

::: warning
`.values()` method known from Python's `dict` class is not currently available
:::

::: tip
Very often simple attribute access is enough to get good key for given element. It is so often, that Gluten allows to specify `key` argument as string, and automatically converts it to [operator.attrgetter](https://docs.python.org/3/library/operator.html#operator.attrgetter). This allows to write code like this:

```python
class BooksIndexedByTitlePage(Page):
    books_by_title_using_lambda_key = LocateMany('.book', webelement_class=BookWebElement, key=lambda book: book.title.text)
    books_by_title_using_string_key = LocateMany('.book', webelement_class=BookWebElement, key='book.title.text')
```

in above example both `books_by_title_using_lambda_key` and `books_by_title_using_string_key` are equivalent.
:::

## Global locators

As previously said, custom webcomponents have search scope, used by it's locators, limited to children of custom webcomponent. Most of time this is great feature, that allows to describe structure of nested elements.

However, sometimes custom webcomponent needs to locate element outside its search scope, that means globaly on webpage
