# work suspended

from selenium import webdriver
from selenium.webdriver.firefox.options import Options


driver = webdriver.Firefox()
url = driver.command_executor._url       #"http://127.0.0.1:60622/hub"
session_id = driver.session_id            #'4e167f26-dc1d-4f51-a207-f761eaf73c31'

driver = webdriver.Remote(command_executor=url,desired_capabilities={})
driver.close()   # this prevents the dummy browser
driver.session_id = session_id

driver.get("http://www.mrsmart.in")