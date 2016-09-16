# felinium

Selenium for cats, or, Chad does not code while other people are watching.

Check the branches to see the examples. Table of contents below; the "chapters"
are actual branch names you can checkout. All Python files are found in the
`felinium` directory.

## 1-quick-demo

Introducing what Selenium does. See `ghostwriter.py`.

Notes:

- `driver.get` waits until the moment the browser's `onload` event has fired.
This is problematic if your page fetches data even after `onload`, say via AJAX.
- What happens when an error occurs before `driver.close()`? How is that relevant
to us?

Links:

- [Selenium Selectors](http://selenium-python.readthedocs.io/locating-elements.html#locating-elements)

## 2-arte-angular

Motivating question: Is our UI too fancy for Selenium?

How to interact with `ui-select-2`/`kb-mobile-prefix-selector`? See `uiselect2.py`

What happens when the selector applies to more than one element? [You can locate
via CSS selectors](https://www.kalibrr.com/employers/signup) but it is still not
as flexible as jQuery. See `multielement.py`.
