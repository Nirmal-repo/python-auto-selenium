import time

from selenium.webdriver.common.by import By

from base.Selenium_Drivers import SeleniumDrivers


class SearchPage(SeleniumDrivers):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    search_input = (By.ID, "search_query_top")
    search_icon = (By.NAME, "submit_search")


    def enterSearchInput(self,text):
        self.sendKeys(self.search_input,text)


    def clickSearchIcon(self):
        self.clickElement(self.search_icon)
        time.sleep(10)

    def validtateSearch(self,product_name):
        print("search started from here....")
        self.enterSearchInput(product_name)
        self.clickSearchIcon()