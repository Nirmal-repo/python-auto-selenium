import os
import time
from traceback import print_stack

from selenium.webdriver.common.by import By
import utilities.Custom_Logger as cl
import logging
import pytest


class SeleniumDrivers:
    log =cl.customLogger(logging.DEBUG)
    def __init__(self,driver):
        self.driver = driver

    locator_type = None
    locatorname = None


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
            self.log.info("Element found  locator: " + self.locatorname + " with locator type is :" + self.locator_type)
        except:
            self.log.info("Element not found  locator: "+ self.locatorname + " with locator type is :" + self.locator_type)
        return element

    def getElementList(self, element_locator):
        element = None
        byType = element_locator[0]
        self.locator_type=byType
        self.locatorname=element_locator[1]
        byType= self.getByType(byType)

        try:
            element = self.driver.find_elements(byType, self.locatorname)
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
            self.log.info("Sent " + data + " on element with locators :" + self.locatorname + " with locator type is :" + self.locator_type)
        except:
            self.log.info("Cannot send data on the element with locator:" + self.locatorname+ " with locator type is :" + self.locator_type)
            print_stack()

    def clickElement(self,locator):
        element = None
        try:
            if locator:
                element = self.getElement(locator)
            element.click()
            self.log.info("clicked on elements with locators :" + self.locatorname + " with locator type is :" + self.locator_type)
        except:
            self.log.info("Cannot click on the  element with locator: " + self.locatorname + " with locator type is :" + self.locator_type)
            print_stack()

    def isElementDisplayed(self,locator):
        element = None
        isDisplayed = False
        try:
            if locator:  # If locator is not empty
                element = self.getElement(locator)
            if element is not None:
                isDisplayed =element.is_displayed()
                print("Element is displayed on the page")
            else:
                print("Element not displayed on the page")
            return isDisplayed
        except:
            print("Element not displayed on the page")
            return False

    def getTitle(self):
        return self.driver.title

    def getText(self,locator):
        element = None;
        try:
            if locator:
                element = self.getElement(locator)
            text =element.text
            if len(text) != 0:
                self.log.info("Getting text on element " + text)
                text =text.strip()
        except:
            self.log.info("Failed to get an element from element ")
            print_stack()
            text = None
        return text

    def screenshot(self,resultMessage):
        """
        Take screenshot of current open webPage if test case fail
        """
        fileName = resultMessage+"."+str(round(time.time()*1000))+".png"
        screenShotDirectory = "../screenshots/"
        relativeFileName =screenShotDirectory +fileName

        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory,relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenShotDirectory)

        try:
            if not os.path.exists((destinationDirectory)):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)

            self.log.info(" screenshot save to the directory " + screenShotDirectory)
        except:
            self.log.error("### Exception Occurred when taking screenshot")
            print_stack()












