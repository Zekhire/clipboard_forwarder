from selenium import webdriver
import os
import json

chrome_dict = json.load(open("./browsers/browsers_data.json"))["chrome"]
print(chrome_dict)

command = chrome_dict["path"]+" -remote-debugging-port="+str(chrome_dict["port"])

os.system('"' + command + '"')