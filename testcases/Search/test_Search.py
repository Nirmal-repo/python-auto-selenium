import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.HomePage import HomePage
from pageObjects.SearchPage import SearchPage


class TestSearch:
    def test_sucessSearch(self):

        baseUrl="http://automationpractice.com/index.php"
        driver = webdriver.Chrome(executable_path="../../drivers/chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(3)
        print("Chrome driver is selected ....")
        driver.get(baseUrl)
        print("page title : " + driver.title)
        homepage = HomePage(driver)
        searchpage=SearchPage(driver)
        searchpage.validtateSearch("skirt")
        driver.quit()







