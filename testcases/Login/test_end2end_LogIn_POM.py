import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.HomePage import HomePage


class TestLogin:
    def test_sucessFullLogin(self):

        baseUrl="http://automationpractice.com/index.php"
        driver = webdriver.Chrome(executable_path="../../drivers/chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(3)
        print("Chrome driver is selected ....")
        driver.get(baseUrl)
        print("page title : " , driver.title)
        homepage = HomePage(driver)
        loginpage = homepage.click_SignIn()
        loginpage .login("nirmal@yopmail.com","jain1985$")

        username = homepage.getAccountName().text
        print("Login sucessfull and user loged in with ", username, "user id ")
        assert username in "Nirmal Jain" ,"User name does not exists or matched ..."
        homepage.click_SignOut()
        driver.quit()

    def test_loginFailed(self):
        baseUrl = "http://automationpractice.com/index.php"
        driver = webdriver.Chrome(executable_path="../../drivers/chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(3)
        print("Chrome driver is selected ....")
        driver.get(baseUrl)
        print("page title : ", driver.title)
        homepage = HomePage(driver)
        loginpage = homepage.click_SignIn()
        loginpage.login(" " ," ")
        errorMsg = loginpage.getErrorMessage_text().text
        print("Error Message :" ,errorMsg)
        assert "An email address required." in errorMsg


