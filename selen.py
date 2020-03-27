from selenium import webdriver
import time
import os
# os.system('cmd /c "\"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe\" -remote-debugging-port=9114 --user-data-dir="D:\SelenTest\Chrome_Test_profile"')
# "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" -remote-debugging-port=9114 --user-data-dir="D:\SelenTest\Chrome_Test_profile"

# C:\Program Files (x86)\Mozilla Firefox\firefox.exe -remote-debugging-port=9014 --user-data-dir="D:\SelenTest\Firefox_Test_profile"
# "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" -remote-debugging-port=9014 --user-data-dir="D:\SelenTest\Chrome_Test_profile"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("debuggerAddress", "localhost:9114")
driver = webdriver.Chrome(executable_path=r'chromedriver.exe', options=chrome_options)

driver.get("https://translate.google.pl/?hl=pl&tab=TT0") # <---
search_input_box = driver.find_element_by_id("source") # <---
search_input_box.send_keys("可愛い")

time.sleep(10)
search_input_box.clear()
search_input_box.send_keys("私は部屋で行った行った")
time.sleep(10)
search_input_box.clear()
search_input_box.send_keys("私のお尻は大きいなお尻")

exit()


# from selenium import webdriver
# # firefox_Profile = webdriver.FirefoxProfile(r'C:\Users\krzys\AppData\Roaming\Mozilla\Firefox\Profiles\dzdn29re.default')
# profile = webdriver.FirefoxProfile()
# profile.add_extension(extension=r"C:\Users\krzys\AppData\Roaming\Mozilla\Firefox\Profiles\dzdn29re.default\extensions\staswolf@gmail.com.xpi")
#
# driver = webdriver.Firefox(firefox_profile=profile, executable_path=r'geckodriver.exe')
# # driver = webdriver.Firefox(firefox_profile=firefox_Profile)
# profile = webdriver.FirefoxProfile()
# # driver.get("https://translate.google.pl/?hl=pl&tab=TT0")
# driver.get("https://google.com")
# exit()



chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("debuggerAddress", "localhost:4001")
# chrome_options.add_argument(r"C:\Users\krzys\AppData\Local\Google\Chrome\User Data\Default")

# chrome_options.add_extension(r"C:\Users\krzys\AppData\Local\Google\Chrome\User Data\Default\Extensions\clidkjbfdlffpbbhlalnkifiehenkjaj\4.0.3_0.crx")
# driver = webdriver.Chrome(executable_path=r'chromedriver.exe', chrome_options=chrome_options)

driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
driver.get("https://translate.google.pl/?hl=pl&tab=TT0") # <---
search_input_box = driver.find_element_by_id("source") # <---


exit()
from selenium import webdriver
from selenium import webdriver
import time


# driver = webdriver.Chrome(executable_path=r'chromedriver.exe')    # <---
# driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
# driver = webdriver.Firefox(executable_path=r'geckodriver.exe')

# ext = r"C:\Users\krzys\AppData\Roaming\Mozilla\Firefox\Profiles\dzdn29re.default\extensions"
# ext = r"C:\Users\krzys\AppData\Roaming\Mozilla\Firefox\Profiles\dzdn29re.default\browser-extension-data"

# driver = webdriver.Firefox(executable_path=r'geckodriver.exe', firefox_profile=ext)
# driver.get("https://google.com")
# driver.get("https://translate.google.pl/?hl=pl&tab=TT0") # <---


# search_input_box = driver.find_element_by_id("source") # <---

print("1")
firefox_Profile = webdriver.FirefoxProfile(r'C:\Users\krzys\AppData\Roaming\Mozilla\Firefox\Profiles\dzdn29re.default')
print("2")
driver = webdriver.Firefox(firefox_Profile)
print("3")
# driver.get("https://translate.google.pl/?hl=pl&tab=TT0")
driver.get("https://google.com")

search_input_box = driver.find_element_by_name("q")
# search_input_box = driver.find_element_by_class_name("source-input")
while True:
    search_input_box.send_keys("可愛い")
    time.sleep(1)
    search_input_box.clear()
    search_input_box.send_keys("愛い")
    time.sleep(1)
    search_input_box.clear()
    search_input_box.send_keys("い")
    search_input_box.clear()
    time.sleep(1)







# # driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
# # driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
# driver = webdriver.Firefox(executable_path=r'geckodriver.exe')
# driver.get("https://google.com")
#
#
#
# search_input_box = driver.find_element_by_name("q")
# search_input_box.send_keys("可")
# time.sleep(1)
# search_input_box.clear()
# search_input_box.send_keys("愛")
# time.sleep(1)
# search_input_box.clear()
# search_input_box.send_keys("い")
#
