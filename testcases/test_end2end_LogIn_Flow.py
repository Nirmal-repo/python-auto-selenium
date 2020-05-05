import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCheckOut:
    def test_loginFlow(self):
        driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(10)
        print("Chrome driver is selected ....")
        driver.get("http://automationpractice.com/index.php")
        print("page title : " , driver.title)
        driver.find_element_by_css_selector(".login").click()
        print("page title : ", driver.title)
        driver.find_element_by_css_selector("#email").send_keys("nirmal@yopmail.com")
        driver.find_element_by_css_selector("#passwd").send_keys("jain1985$")
        driver.find_element_by_css_selector("#SubmitLogin").click()
        driver.find_element_by_css_selector(".account").is_displayed()
        username= driver.find_element_by_css_selector(".account").text
        print("user name :" ,username)
        assert username in "Nirmal Jain"
        driver.find_element_by_css_selector(".logout").click()
        driver.find_element_by_css_selector(".login").is_displayed()
        driver.quit()


