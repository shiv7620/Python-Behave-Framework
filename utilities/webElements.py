from selenium.common.exceptions import NoSuchElementException
from pageObjects.application import app

def isElementExists(xpath):

    driver = app.get_driver()
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False

    return True
