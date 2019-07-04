
from selenium.webdriver.common.by import By

from pageObjects.application import app
from utilities.webElements import isElementExists
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login():

    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Login()
        return cls.instance

    def __init__(self):
        print("Getting driver instance")
        self.driver = app.get_driver()

    def mercuryLogin(self, userName, password):

        # Defining the web elements
        tbox_UserName = self.driver.find_element_by_css_selector("input[name='userName']")
        tbox_Password = self.driver.find_element_by_css_selector("input[name='password']")
        btn_SignIn = self.driver.find_element_by_css_selector("input[name='login']")

        # Verifying the correct page is loaded
        assert tbox_UserName.is_displayed(), "Login page is loaded"

        # Login
        tbox_UserName.send_keys(userName)
        tbox_Password.send_keys(password)
        btn_SignIn.click()

        # Explicit wait for a element
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[text()='SIGN-OFF']")))
        assert isElementExists("//a[text()='SIGN-OFF']"), "Login is successful"


    def mercuryLogout(self):

        lnk_SignOff = self.driver.find_element_by_link_text("SIGN-OFF")
        lnk_SignOff.click()

        isExists = isElementExists("//a[text()='SIGN-ON']")

        assert isElementExists("//a[text()='SIGN-ON']"), "Logout is successful"

loginPage = Login.get_instance()
