from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


from selenium import webdriver

driver = webdriver.Firefox()
executor_url = driver.command_executor._url
session_id = driver.session_id
driver.get("http://tarunlalwani.com")

print(session_id)
print(executor_url)

def create_driver_session(session_id, executor_url):
    from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

    # Save the original function, so we can revert our patch
    org_command_execute = RemoteWebDriver.execute

    def new_command_execute(self, command, params=None):
        if command == "newSession":
            # Mock the response
            return {'success': 0, 'value': None, 'sessionId': session_id}
        else:
            return org_command_execute(self, command, params)

    # Patch the function before creating the driver object
    RemoteWebDriver.execute = new_command_execute

    new_driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
    new_driver.session_id = session_id

    # Replace the patched function with original function
    RemoteWebDriver.execute = org_command_execute

    return new_driver

driver2 = create_driver_session(session_id, executor_url)
print(driver2.current_url)
exit()
# driver = webdriver.Firefox()
#
# url = driver.command_executor._url       #"http://127.0.0.1:60622/hub"
# session_id = driver.session_id            #'4e167f26-dc1d-4f51-a207-f761eaf73c31'
#
# driver = webdriver.Remote(command_executor=url,desired_capabilities={})
# driver.session_id = session_id
#
# driver.get("http://www.mrsmart.in")
#
# exit()




# executor_url = driver.command_executor._url
# session_id = driver.session_id

def attach_to_session(executor_url, session_id):
    original_execute = WebDriver.execute
    def new_command_execute(self, command, params=None):
        if command == "newSession":
            # Mock the response
            return {'success': 0, 'value': None, 'sessionId': session_id}
        else:
            return original_execute(self, command, params)
    # Patch the function before creating the driver object
    WebDriver.execute = new_command_execute
    driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
    driver.session_id = session_id
    # Replace the patched function with original function
    WebDriver.execute = original_execute
    return driver

bro = attach_to_session('http://127.0.0.1:64092', '8de24f3bfbec01ba0d82a7946df1d1c3')
bro.get('https://translate.google.pl/?hl=pl&tab=TT0')