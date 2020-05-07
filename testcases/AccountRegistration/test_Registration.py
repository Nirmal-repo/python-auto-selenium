import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from pageObjects.HomePage import HomePage
import utilities.Custom_Logger as cl
import logging
import pytest

@pytest.mark.usefixtures("setUp")
class TestAccountRegistration:
    log = cl.customLogger(logging.DEBUG)
    def test_existingUserRegistered(self):

        homepage = HomePage(self.driver)
        self.log.info("Chrome driver is selected ....")
        self.log.info("page title : " , self.driver.title)
        accountregister = AccountRegistrationPage(self.driver)
        loginpage = homepage.click_SignIn()
        accountregister.enterRegisteredEmail("nirmal@yopmail.com")
        registeredMessage = accountregister.getExistingUserMsg().text
        self.log.info("All ready Registered Message : ", registeredMessage)
        assert registeredMessage in accountregister.duplicateMsg




