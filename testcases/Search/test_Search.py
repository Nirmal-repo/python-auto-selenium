import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


from pageObjects.HomePage import HomePage
from pageObjects.SearchPage import SearchPage
import logging
import utilities.Custom_Logger as cl
from utilities.TestStatus import  TestStatus

@pytest.mark.usefixtures("setUp")
class TestSearch:
    log = cl.customLogger(logging.DEBUG)
    def test_sucessSearch(self):

        self.log.info("Chrome driver is selected ....")
        self.log.info("page title : " + self.driver.title)
        homepage = HomePage(self.driver)
        searchpage=SearchPage(self.driver)
        ts=TestStatus(self.driver)
        result1 =searchpage.searchInput_text()
        ts.setResult(result1,"Search Input text not present")

       # assert result1 == True
        print("Search input text box verification is (result 1): ", result1)
        searchpage.validtateSearch("skirt")
        result2= searchpage.verifyPageTitle()
        ts.setResult(result2, "Title page not matched...")
        print("page result assertion value is (result 2): ", result2)
        assert result2 == True
        time.sleep(5)
        result3 = searchpage.validateSearchCount()
        ts.setResult(result3, "Search count is less than 1 ")
        print("Search Count assertion is (result 3) : " ,result3)
        assert result3 == True








