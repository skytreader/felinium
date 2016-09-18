# felinium

Selenium for cats, or, Chad does not code while other people are watching. This
was not designed without Chad speaking in the background.

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
for unit testing?

Links:

- [Selenium Selectors](http://selenium-python.readthedocs.io/locating-elements.html#locating-elements)

# Arte Angular

Motivating question: Is our UI too fancy for Selenium? For instance, dealing with
`select` elements is easy---see `plain_select.py`.

But we use `ui-select2`! What do? See `uiselect2.py`

What happens when the selector applies to more than one element? [You can locate
via CSS selectors](https://www.kalibrr.com/employers/signup) but it is still not
as flexible as jQuery. You could use XPath but it is messy. jQuery is the bestest!!!!111!
See `multielement.py`.

How about links that open new tabs/windows, of which we have plenty?! See
`new_window.py`. But, just by using the code we have now, this is prone to
memory leaks.

## Logging-in

(Source not included.)

There are two ways:

1. Log-in "like a real user" by loading the log-in page, selecting input boxes,
and sending them your user credentials.
2. [Setting the cookies for yourself](http://selenium-python.readthedocs.io/navigating.html#cookies).

## Miscellaneous stuff that may come in useful

- As a real user, you can execute JavaScript in the browser's console. In
Selenium, you can do the same via the driver's `execute_async_script` and
`execute_script` methods.
- Selenium does not play well with unexpected browser dialogs (alerts, prompts,
etc.).

# Unit Testing
