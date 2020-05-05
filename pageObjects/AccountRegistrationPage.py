from selenium.webdriver.common.by import By


class AccountRegistrationPage:

    def __init__(self, driver):
        self.driver = driver

    emailAddress_input= (By.CSS_SELECTOR,"#email_create")
    createAccount_button = (By.CSS_SELECTOR,"#SubmitCreate")
    existingUserMsg_text = (By.CSS_SELECTOR, "#create_account_error li")
    duplicateMsg="An account using this email address has already been registered. Please enter a valid password or request a new one. "

    def getEmailAddressInput(self):
        return self.driver.find_element(*AccountRegistrationPage.emailAddress_input)
    def getCreateAccountButton(self):
        return self.driver.find_element(*AccountRegistrationPage.createAccount_button)
    def getExistingUserMsg(self):
        return self.driver.find_element(*AccountRegistrationPage.existingUserMsg_text)

    def enterRegisteredEmail(self,emailId):
        self.getEmailAddressInput().send_keys(emailId)
        self.getCreateAccountButton().click()
