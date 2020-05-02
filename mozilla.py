# from selenium import webdriver
# firefox_Profile = webdriver.FirefoxProfile(r'C:\Users\krzys\AppData\Roaming\Mozilla\Firefox\Profiles\dzdn29re.default')
# driver = webdriver.Firefox(firefox_Profile)
# # driver.get("https://translate.google.pl/?hl=pl&tab=TT0")
# #driver.get("https://google.com")


from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# ext0 = "{0AA9101C-D3C1-4129-A9B7-D778C6A17F82}.xpi"
# ext1 = "staswolf@gmail.com.xpi"
# ext2 = "{59812185-ea92-4cca-8ab7-cfcacee81281}.xpi"
# profile = webdriver.FirefoxProfile()
# profile.add_extension(extension=ext0)
# profile.add_extension(extension=ext1)
# profile.add_extension(extension=ext2)
# driver = webdriver.Firefox(firefox_profile=profile)
# driver.get("https://translate.google.pl/?hl=pl&tab=TT0")
# search_input_box = driver.find_element_by_id("source")
# search_input_box.send_keys("dupa") 


# profile = webdriver.FirefoxProfile(r"C:\Users\krzys\AppData\Roaming\Mozilla\Firefox\Profiles\dzdn29re.default")
# driver = webdriver.Firefox(firefox_profile=profile)
# driver.get("https://translate.google.pl/?hl=pl&tab=TT0")
# search_input_box = driver.find_element_by_id("source")
# search_input_box.send_keys("dupa")   


driver = webdriver.Firefox()
url = driver.command_executor._url       #"http://127.0.0.1:60622/hub"
session_id = driver.session_id            #'4e167f26-dc1d-4f51-a207-f761eaf73c31'

driver = webdriver.Remote(command_executor=url,desired_capabilities={})
driver.close()   # this prevents the dummy browser
driver.session_id = session_id

driver.get("http://www.mrsmart.in")