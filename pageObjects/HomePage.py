from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
import logging
import utilities.Custom_Logger as cl


class HomePage():
    log = cl.customLogger(logging.DEBUG)
    def __init__(self,driver):
        self.driver = driver

    signIn_link = (By.CSS_SELECTOR,".login")
    signOut_link =(By.CSS_SELECTOR,".logout")
    contactus_link = (By.CSS_SELECTOR,"#contact-link a")
    search_input = (By.CSS_SELECTOR,"#search_query_top"	)
    search_icon = (By.CSS_SELECTOR, "button[name='submit_search']")
    accountname_text = (By.CSS_SELECTOR,".account")


    def getSignInLink(self):
        return self.driver.find_element(*HomePage.signIn_link)

    def getSignOutLink(self):
        return self.driver.find_element(*HomePage.signOut_link)

    def getContactUsLink(self):
        return self.driver.find_element(*HomePage.contactus_link)

    def getSearchInput(self):
        return self.driver.find_element(*HomePage.search_input)

    def getSearchButton(self):
        return self.driver.find_element(*HomePage.search_icon)

    def getAccountName(self):
        return self.driver.find_element(*HomePage.accountname_text)



    def click_SignIn(self):
       # self.driver.find_element_by_css_selector(".login").click()
        self.getSignInLink().click()
        print("page title : ", self.driver.title)
        loginpage= LoginPage(self.driver)
        return loginpage

    def click_SignOut(self):
        self.getSignOutLink().click()
        loginpage = LoginPage(self.driver)
        return loginpage


    def verifyIsUserNameDisplayed(self):

        return self.getAccountName().is_displayed()

