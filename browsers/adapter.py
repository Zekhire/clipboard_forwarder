import browsers.chrome
import browsers.opera


def open_browser(browsers_data):
    browser = browsers_data["browser"]
    if browser == "chrome":
        browsers.chrome.open_browser(browsers_data["chrome"])
    elif browser == "opera":
        browsers.opera.open_browser(browsers_data["opera"])


def open_page(browsers_data):
    browser = browsers_data["browser"]
    if browser == "chrome":
        text_input_box = browsers.chrome.open_page(browsers_data["chrome"])
    elif browser == "opera":
        text_input_box = browsers.opera.open_page(browsers_data["opera"])
    return text_input_box