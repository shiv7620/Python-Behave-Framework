# application.py
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utilities.GlobalVariables import projectPath, SuiteType


class Application:

    instance = None

    @classmethod
    def get_instance(cls):
        # This is class method.
        # It checks if instance is empty and creates instance of this class
        if cls.instance is None:
            cls.instance = Application()
        return cls.instance

    def __init__(self):
        # This is constructor

        if SuiteType == "API":
            self.driver = None
        else:
            # Getting chrome driver path
            chrome_path = os.path.join(projectPath, 'resources\\chromedriver.exe')

            # Setting chrome necessary chrome options
            chrome_options = Options()
            chrome_options.add_argument("--disable-extensions")

            # Launching chrome and maximizing browser
            self.driver = webdriver.Chrome(executable_path=chrome_path, chrome_options=chrome_options)
            self.driver.set_page_load_timeout(15)
            self.driver.maximize_window()


    def get_driver(self):
        # Returning driver instance , to be used in page objects
        return self.driver

    def close_driver(self):
        # Closing current driver windows
        return self.driver.close()

    def load_website(self, url):
        # This method launches URL.
        self.driver.get(url)


app = Application.get_instance()
