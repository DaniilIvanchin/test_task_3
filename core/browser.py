from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Browser:
    def __init__(self, options_list=None):
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()

        if options_list:
            for arg in options_list:
                options.add_argument(arg)

        self.driver = webdriver.Chrome(service=service, options=options)

    def quit(self):
        self.driver.quit()