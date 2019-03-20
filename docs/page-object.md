
## Core concepts


### Page Object

Page Object Pattern is centered about Page Object concept. Page Object describes how page is build, what elements does it contain. Additionally it allows to access those elements and interact with them using complex actions.

All Page objects created using Gluten are created by inheriting from `gluten.page.Page` base class. The simplest, empty Page object looks like this:

```python
from gluten import Page


class EmptyPageObject(Page):
    pass
```
