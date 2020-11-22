from selenium import webdriver

def open_browser(opera_dict):
    pass


def open_page(opera_dict):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('--remote-debugging-port=9222')
    #options.add_argument("user-data-dir=D:\\SelenTest\\Opera_test_profile")
    options.add_argument("user-data-dir="+opera_dict["profile"])
    # driver = webdriver.Opera(options=options, executable_path=r'.\\operadriver\\operadriver.exe')
    driver = webdriver.Opera(options=options, executable_path=opera_dict["driver"])
    driver.get("https://translate.google.pl/?hl=pl&tab=TT0")
    text_input_box = driver.find_element_by_id("source")
    return text_input_box
