from selenium import webdriver
import os

def open_browser(chrome_dict):
    command = chrome_dict["path"]+" -remote-debugging-port="+str(chrome_dict["port"])+" --user-data-dir="+chrome_dict["profile"]
    os.system('"' + command + '"')


def open_page(chrome_dict):
    translator_url = "https://translate.google.pl/?hl=pl&tab=TT0"
    text_input_tag = "textarea"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("debuggerAddress", "localhost:9114")
    #driver = webdriver.Chrome(executable_path=r'../chromedriver.exe', options=chrome_options)
    driver = webdriver.Chrome(executable_path=chrome_dict["driver"], options=chrome_options)
    driver.get(translator_url)
    text_input_box = driver.find_element_by_tag_name(text_input_tag)
    return text_input_box