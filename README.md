# Wagtail Multiple Chooser Panel

An InlinePanel variant allowing multiple items to be quickly selected

[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![PyPI version](https://badge.fury.io/py/wagtail-multiple-chooser-panel.svg)](https://badge.fury.io/py/wagtail-multiple-chooser-panel)
[![Multiple Chooser Panel CI](https://github.com/wagtail/wagtail-multiple-chooser-panel/actions/workflows/test.yml/badge.svg)](https://github.com/wagtail/wagtail-multiple-chooser-panel/actions/workflows/test.yml)

## About

This package provides an improved user interface for the common setup of a chooser widget inside an InlinePanel - for example, an image gallery consisting of a list of images chosen from the Wagtail image library. Normally, this would require adding a new child form for each item, opening the chooser modal and selecting an individual item each time. With the `MultipleChooserPanel` provided by this package, the "Add item" button now opens the chooser modal immediately, with the ability to select multiple items - all selected items are then added as child forms.

![Example of MultipleChooserPanel in use on a blog page on the bakery demo site: the user clicks "Add author(s)", opening up a person chooser with checkboxes against each name. The user ticks the boxes for Muddy Waters and Olivia Ava, then clicks "Confirm selection" - this results in Muddy Waters and Olivia Ava being added as authors for the blog page.](docs/multiple-chooser-panel.gif)

In this version, only choosers implemented via [wagtail-generic-chooser](https://github.com/wagtail/wagtail-generic-chooser) are supported; it is planned that this functionality will be incorporated into a future Wagtail release, with support for all of Wagtail's built-in choosers as well as custom choosers created through [ChooserViewSet](https://docs.wagtail.org/en/stable/extending/generic_views.html#chooserviewset).

## Links

- [Documentation](https://github.com/wagtail/wagtail-multiple-chooser-panel/blob/main/README.md)
- [Changelog](https://github.com/wagtail/wagtail-multiple-chooser-panel/blob/main/CHANGELOG.md)
- [Contributing](https://github.com/wagtail/wagtail-multiple-chooser-panel/blob/main/CHANGELOG.md)
- [Discussions](https://github.com/wagtail/wagtail-multiple-chooser-panel/discussions)
- [Security](https://github.com/wagtail/wagtail-multiple-chooser-panel/security)

## Supported versions

- Python 3.7 - 3.11
- Django 3.2 - 4.1
- Wagtail 4.1

## Installation

- Ensure you have [wagtail-generic-chooser](https://github.com/wagtail/wagtail-generic-chooser) version 0.5 or above installed
- `pip install wagtail-multiple-chooser-panel`
- Add `"wagtail_multiple_chooser_panel"` to INSTALLED_APPS

## Usage

Beginning from an `InlinePanel` setup where the child model has a field with a chooser widget defined through `wagtail-generic-chooser`, such as:

```python
class BlogPersonRelationship(Orderable, models.Model):
    page = ParentalKey(
        "BlogPage", related_name="blog_person_relationship", on_delete=models.CASCADE
    )
    person = models.ForeignKey(
        "base.Person", related_name="person_blog_relationship", on_delete=models.CASCADE
    )
    panels = [FieldPanel("person", widget=PersonChooser)]


class BlogPage(Page):
    content_panels = Page.content_panels + [
        # ...
        InlinePanel(
            "blog_person_relationship",
            label="Author(s)", min_num=1
        ),
    ]
```

Import `MultipleChooserPanel` from `wagtail_multiple_chooser_panel.panels`, replace `InlinePanel` with `MultipleChooserPanel`, and add a new `chooser_field_name` parameter that specifies the field of the child model that has the chooser widget:

```python
from wagtail_multiple_chooser_panel.panels import MultipleChooserPanel

# BlogPersonRelationship definition remains unchanged

class BlogPage(Page):
    content_panels = Page.content_panels + [
        # ...
        MultipleChooserPanel(
            "blog_person_relationship",
            chooser_field_name="person",
            label="Author(s)", min_num=1
        ),
    ]
```