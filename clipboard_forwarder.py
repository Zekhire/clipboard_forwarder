from selenium import webdriver
from tkinter import Tk
from time import time
import threading
import browsers.adapter
import json


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


def forwarder(browsers_data, rem_inc=False, interval=0.25, show=False):
    text_input_box = browsers.adapter.open_page(browsers_data)
    old_dialog = "sofhiudsgf7ieghfuisdgofhdsiuhfdsihjfoisdgiofjsuifhsdoihfyusdghip"
    time_start = time()

    while True:
        time_stop = time()
        if time_stop - time_start > interval:
            if show:
                print("tick")

            try:
                dialog = Tk().clipboard_get()
            except:
                continue

            if dialog != old_dialog:
                if rem_inc:
                    dialog_cleaned = remove_inconvenient(dialog)

                text_input_box.clear()
                text_input_box.send_keys(dialog_cleaned)    
                old_dialog = dialog

            time_start = time_stop


def forwarder_foyer(browsers_data):
    t1 = threading.Thread(target=browsers.adapter.open_browser, args=[browsers_data]) 
    t2 = threading.Thread(target=forwarder, args=[browsers_data]) 

    t1.start()
    t2.start() 

    t1.join()
    t2.join() 


if __name__ == "__main__":
    browsers_data = json.load(open("./browsers_data.json"))
    forwarder_foyer(browsers_data)