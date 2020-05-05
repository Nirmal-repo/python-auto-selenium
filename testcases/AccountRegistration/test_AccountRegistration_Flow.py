import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from pageObjects.HomePage import HomePage


class TestAccountRegistration:
    def test_existingUserRegistered(self):
        baseUrl="http://automationpractice.com/index.php"
        driver = webdriver.Chrome(executable_path="../../drivers/chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(3)
        print("Chrome driver is selected ....")
        driver.get(baseUrl)
        print("page title : " , driver.title)

        homepage = HomePage(driver)
        accountregister = AccountRegistrationPage(driver)
        loginpage = homepage.click_SignIn()
        accountregister.enterRegisteredEmail("nirmal@yopmail.com")
        registeredMessage = accountregister.getExistingUserMsg().text
        print("All ready Registered Message : ", registeredMessage)
        assert registeredMessage in accountregister.duplicateMsg



