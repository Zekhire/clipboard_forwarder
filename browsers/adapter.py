import browsers.chrome
import browsers.opera
import json

def open_browser(browser):
    data = json.load(open("./browsers/browsers_data.json"))
    if browser == "chrome":
        browsers.chrome.open_browser(data["chrome"])
    elif browser == "opera":
        browsers.opera.open_browser(data["opera"])


def open_page(browser):
    data = json.load(open("./browsers/browsers_data.json"))
    if browser == "chrome":
        search_input_box = browsers.chrome.open_page(data["chrome"])
    elif browser == "opera":
        search_input_box = browsers.opera.open_page(data["opera"])
    return search_input_box