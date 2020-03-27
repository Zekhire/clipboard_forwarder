import numpy as np
from selenium import webdriver
from tkinter import Tk
from time import time

def open_browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("debuggerAddress", "localhost:9114")
    driver = webdriver.Chrome(executable_path=r'chromedriver.exe', options=chrome_options)
    driver.get("https://translate.google.pl/?hl=pl&tab=TT0")  # <---
    search_input_box = driver.find_element_by_id("source")  # <---
    return search_input_box


def remove_inconvenient(dialog):
    dialog_cleaned = dialog
    while True:
        left = dialog_cleaned.find("<")
        right = dialog_cleaned.find(">")
        if left == -1 or right == -1:
            break
        else:
            dialog_cleaned = dialog_cleaned[:left] + dialog_cleaned[right+1:]
    return dialog_cleaned


def forwarder(interval=1):
    search_input_box = open_browser()
    old_dialog = "sofhiudsgf7ieghfuisdgofhdsiuhfdsihjfoisdgiofjsuifhsdoihfyusdghip"
    time_start = time()
    while True:
        time_stop = time()
        if time_stop - time_start > interval:
            dialog = Tk().clipboard_get()
            print("tick")
            if dialog != old_dialog:
                dialog_cleaned = remove_inconvenient(dialog)
                search_input_box.clear()
                search_input_box.send_keys(dialog_cleaned)    
                old_dialog = dialog
            time_start = time_stop



if __name__ == "__main__":
    forwarder()