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

@pytest.mark.usefixtures("setUp")
class TestSearch:
    log = cl.customLogger(logging.DEBUG)
    def test_sucessSearch(self):

        self.log.info("Chrome driver is selected ....")
        self.log.info("page title : " + self.driver.title)
        homepage = HomePage(self.driver)
        searchpage=SearchPage(self.driver)
        searchpage.validtateSearch("skirt")








