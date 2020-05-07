import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.HomePage import HomePage
import logging
import utilities.Custom_Logger as cl
import pytest

@pytest.mark.usefixtures("setUp")
class TestLogin:
    log = cl.customLogger(logging.DEBUG)
    def test_sucessFullLogin(self):

        homepage = HomePage(self.driver)
        self.log.info("Chrome driver is selected ....")
        self.log.info("page title : " , self.driver.title)
        loginpage = homepage.click_SignIn()
        loginpage.login("nirmal@yopmail.com","jain1985$")
        assert homepage.verifyIsUserNameDisplayed() == True
        username = homepage.getAccountName().text
        self.log.info("Login sucessfull and user loged in with ", username, "user id ")
        assert username in "Nirmal Jain" ,"User name does not exists or matched ..."
        homepage.click_SignOut()


    def test_loginFailed(self):
        homepage = HomePage(self.driver)
        self.log.info("Chrome driver is selected ....")
        self.log.info("page title : ", self.driver.title)
        loginpage = homepage.click_SignIn()
        loginpage.login(" " ," ")
        errorMsg = loginpage.getErrorMessage_text().text
        self.log.info("Error Message :" ,errorMsg)
        assert "An email address required." in errorMsg



