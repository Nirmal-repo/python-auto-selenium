from traceback import print_stack

from selenium.webdriver.common.by import By


class SeleniumDrivers:
    def __init__(self,driver):
        self.driver = driver

    locator_type= None
    locatorname=None


    def getByType(self,locatorType):
        locatorType=locatorType.lower()
        if locatorType =="id":
            return By.ID
        elif locatorType =="name":
            return By.NAME
        elif locatorType =="xpath":
            return By.XPATH
        elif locatorType =="css selector":
            return By.CSS_SELECTOR
        elif locatorType =="linkText":
            return By.LINK_TEXT
        elif locatorType =="classname":
            return By.CLASS_NAME
        else:
            print("Locator type "+locatorType+ "not corrected/supported.")

        return  False


    def getElement(self, element_locator):
        element = None
        byType = element_locator[0]
        self.locator_type=byType
        self.locatorname=element_locator[1]
        byType= self.getByType(byType)

        try:
            element = self.driver.find_element(byType, self.locatorname)
            print("Element found  locator: " + self.locatorname + " with locator type is :" + self.locator_type)
        except:
            print("Element not found  locator: "+ self.locatorname + " with locator type is :" + self.locator_type)
        return element

    def sendKeys(self,locator,data):
        element = None
        try:
            if locator:
                element = self.getElement(locator)
            element.send_keys(data)
            print("Sent " + data + " on element with locators :" + self.locatorname + " with locator type is :" + self.locator_type)
        except:
            print("Cannot send data on the element with locator:" + self.locatorname+ " with locator type is :" + self.locator_type)
            print_stack()

    def clickElement(self,locator):
        element = None
        try:
            if locator:
                element = self.getElement(locator)
            element.click()
            print("clicked on elements with locators :" + self.locatorname + " with locator type is :" + self.locator_type)
        except:
            print("Cannot click on the  element with locator: " + self.locatorname + " with locator type is :" + self.locator_type)
            print_stack()





