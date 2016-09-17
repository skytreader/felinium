# felinium

Selenium for cats, or, Chad does not code while other people are watching.

Set-up

    mkvirtualenv selenium
    pip install -r requirements.txt
    cd html
    python -m SimpleHTTPServer 16981 > /dev/null 2>&1&
    cd ..

Or you can leave `SimpleHTTPServer` running in anoher terminal tab.

# Quick Demo

Introducing what Selenium does. See `ghostwriter.py`.

Notes:

- `driver.get` waits until the moment the browser's `onload` event has fired.
This is problematic if your page fetches data even after `onload`, say via AJAX.
- What happens when an error occurs before `driver.close()`? How is that relevant
to us?

Links:

- [Selenium Selectors](http://selenium-python.readthedocs.io/locating-elements.html#locating-elements)

# Arte Angular

Motivating question: Is our UI too fancy for Selenium? For instance, dealing with
`select` elements is easy---see `plain_select.py`.

But we use `ui-select2`! What do? See `uiselect2.py`

What happens when the selector applies to more than one element? [You can locate
via CSS selectors](https://www.kalibrr.com/employers/signup) but it is still not
as flexible as jQuery. You could use XPath but it is messy. jQuery is the best.
See `multielement.py`.
