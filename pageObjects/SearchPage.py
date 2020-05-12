import time
import logging
import utilities.Custom_Logger as cl
from selenium.webdriver.common.by import By

from base.Selenium_Drivers import SeleniumDrivers
import utilities.Custom_Logger as cl


class SearchPage(SeleniumDrivers):
    log = cl.customLogger(logging.DEBUG)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    search_input = (By.ID, "search_query_top")
    search_icon = (By.NAME, "submit_search")
    searchCount_label = (By.CSS_SELECTOR,".heading-counter")


    def searchInput_text(self):
        return self.isElementDisplayed(self.search_input)

    def enterSearchInput(self,text):
        self.sendKeys(self.search_input,text)


    def clickSearchIcon(self):
        self.clickElement(self.search_icon)
        time.sleep(10)

    def validtateSearch(self,product_name):
        print("search started from here....")
        self.enterSearchInput(product_name)
        self.clickSearchIcon()

    def validateSearchCount(self):
        status = False
        text =self.getText(self.searchCount_label)
        print("text value is :" + text)
        text= text.split()
        number = int(text[0])

        if number >= 0:
            print("search is sucessfull with result count :" ,number)
            status = True
            return status
        else:
            number = 0
            print("search is not sucessfull  with result count :" ,number)
            return status

    def verifyPageTitle(self):
        if "Search - My Storess" in self.getTitle():
            print("page title is " ,self.getTitle())
            return True
        else:
            return False
