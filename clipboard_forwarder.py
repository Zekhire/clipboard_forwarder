import numpy as np
from selenium import webdriver
from tkinter import Tk
from time import time
import os
import threading

# "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" -remote-debugging-port=9114 --user-data-dir="D:\SelenTest\Chrome_Test_profile"


def open_browser():
    command = '"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe\" -remote-debugging-port=9114 --user-data-dir=\"D:\\SelenTest\\Chrome_Test_profile\"'
    os.system('"' + command + '"')


def wait_for_browser(interval=6):
    time_start = time()
    while True:
        if time() - time_start > interval:
            break



def open_page():
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
    search_input_box = open_page()
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
    t1 = threading.Thread(target=open_browser) 
    t2 = threading.Thread(target=forwarder) 

    t1.start()
    t2.start() 

    t1.join()
    t2.join() 

if __name__ == "__main__":
    forwarder_foyer()