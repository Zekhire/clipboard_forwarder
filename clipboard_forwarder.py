import numpy as np
from selenium import webdriver
from tkinter import Tk
from time import time
import threading
import browsers.adapter

# "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" -remote-debugging-port=9114 --user-data-dir="D:\SelenTest\Chrome_Test_profile"


def wait_for_browser(interval=6):
    time_start = time()
    while True:
        if time() - time_start > interval:
            break



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


def forwarder(browser, interval=1):
    search_input_box = browsers.adapter.open_page(browser)
    old_dialog = "sofhiudsgf7ieghfuisdgofhdsiuhfdsihjfoisdgiofjsuifhsdoihfyusdghip"
    time_start = time()
    while True:
        time_stop = time()
        if time_stop - time_start > interval:
            print("tick")
            try:
                dialog = Tk().clipboard_get()
            except:
                continue

            if dialog != old_dialog:
                dialog_cleaned = remove_inconvenient(dialog)
                search_input_box.clear()
                search_input_box.send_keys(dialog_cleaned)    
                old_dialog = dialog
            time_start = time_stop


def forwarder_foyer():
    browser = "opera"
    t1 = threading.Thread(target=browsers.adapter.open_browser, args=[browser]) 
    t2 = threading.Thread(target=forwarder, args=[browser]) 

    t1.start()
    t2.start() 

    t1.join()
    t2.join() 

if __name__ == "__main__":
    forwarder_foyer()