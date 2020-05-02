import time

# from selenium import webdriver

# webdriver_service = service.Service('.\operadriver\operadriver.exe')
# webdriver_service.start()

# driver = webdriver.Remote(webdriver_service.service_url, webdriver.DesiredCapabilities.OPERA)

# driver.get('https://www.google.com/')
# input_txt = driver.find_element_by_name('q')
# input_txt.send_keys('operadriver\n')

# time.sleep(5) #see the result
# driver.quit()




#command = '"C:\\Users\\krzys\\AppData\\Local\\Programs\\Opera\\launcher.exe\" -remote-debugging-port=9114 --user-data-dir=\"D:\\SelenTest\\Opera_test_profile\"'


# opera_options = webdriver.ChromeOptions()
# opera_options.add_experimental_option("debuggerAddress", "localhost:9114")
# opera_options.binary_location = "C:\\Users\\krzys\\AppData\\Local\\Programs\\Opera\\launcher.exe"
# driver = webdriver.Opera(executable_path="./operadriver/operadriver.exe", options=opera_options)
# driver.get("https://translate.google.pl/?hl=pl&tab=TT0")  # <---
# search_input_box = driver.find_element_by_id("source")  # <---

#CLOSE????
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("debuggerAddress", "localhost:9114")
# driver = webdriver.Chrome(executable_path="./operadriver/operadriver.exe", options=chrome_options)
# driver.get("https://translate.google.pl/?hl=pl&tab=TT0")  # <---
# search_input_box = driver.find_element_by_id("source")  # <---


# import selenium
# from selenium import webdriver
# options = webdriver.ChromeOptions()
# options.binary_location = "C:\\Users\\krzys\\AppData\\Local\\Programs\\Opera\\launcher.exe"
# driver = webdriver.Opera(executable_path="./operadriver/operadriver.exe", options=options) # success!





# from selenium import webdriver
# from selenium.webdriver.chrome import service

# from bs4 import BeautifulSoup

# webdriver_service = service.Service('operadriver/operadriver.exe')
# webdriver_service.start()

# capabilities = { 'operaOptions': { 'debuggerAddress': "localhost:9114" }}

# driver = webdriver.Remote(webdriver_service.service_url, capabilities)

# driver.get('https://www.google.com/')

# input_txt = driver.find_element_by_name('q')
# input_txt.send_keys('operadriver\n')

# soup = BeautifulSoup(driver.page_source, 'html.parser')

# print(soup.title.string)
# print("---")
# for site in soup.find_all('h3'):
#     for child in site.children:
#         print(child.string)
#         print(child['href'])

# driver.quit()



# import webbrowser

# urL='https://translate.google.pl/?hl=pl'
# opera_path = 'C:\\Users\\krzys\\AppData\\Local\\Programs\\Opera\\launcher.exe'
# webbrowser.register('opera', None, webbrowser.BackgroundBrowser(opera_path))
# webbrowser.get('opera').open_new_tab(urL)


from selenium import webdriver
from selenium.webdriver.opera.options import Options

# options = Options()
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument('--headless')
# options.binary_location = r'C:\\Users\\krzys\\AppData\\Local\\Programs\\Opera\\launcher.exe'
# driver = webdriver.Opera(options=options, executable_path=r'.\\operadriver\\operadriver.exe')
# driver.get("http://google.com/")



options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('--disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument('--remote-debugging-port=9222')
options.add_argument(r"user-data-dir=D:\SelenTest\Opera_test_profile")
driver = webdriver.Opera(options=options, executable_path=r'.\\operadriver\\operadriver.exe')
driver.get("https://translate.google.pl/?hl=pl&tab=TT0")
search_input_box = driver.find_element_by_id("source")
search_input_box.send_keys("可愛い野菜理解料理夏季")
time.sleep(5) 