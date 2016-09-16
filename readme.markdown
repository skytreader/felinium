# felinium

Selenium for cats, or, Chad does not code while other people are watching.

Check the branches to see the examples. Table of contents below.

## 1-quick-demo

Introducing what Selenium does.

Notes:

- `driver.get` waits until the moment the browser's `onload` event has fired.
This is problematic if your page fetches data even after `onload`, say via AJAX.
- What happens when an error occurs before `driver.close()`? How is that relevant
to us?

Links:

- [Selenium Selectors](http://selenium-python.readthedocs.io/locating-elements.html#locating-elements)
