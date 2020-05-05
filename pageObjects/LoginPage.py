from selenium.webdriver.common.by import By


class LoginPage():
    def __init__(self,driver):
        self.driver = driver

    emailid_input = (By.CSS_SELECTOR,"#email")
    password_input = (By.CSS_SELECTOR, "#passwd")
    forgetPassword_link = (By.CSS_SELECTOR, "p[class*=lost_password] a")
    signIn_button = (By.CSS_SELECTOR, "#SubmitLogin")
    loginError_message = (By.XPATH,"//div[@class='alert alert-danger']/ol")

    def getEmailId_input(self):
        return self.driver.find_element(*LoginPage.emailid_input)

    def getPassword_input(self):
        return self.driver.find_element(*LoginPage.password_input)

    def getForgetPassword_link(self):
        return self.driver.find_element(*LoginPage.forgetPassword_link)

    def getSignIn_button(self):
        return self.driver.find_element(*LoginPage.signIn_button)

    def getSignIn_button(self):
        return self.driver.find_element(*LoginPage.signIn_button)


    def getErrorMessage_text(self):
        return self.driver.find_element(*LoginPage.loginError_message)

    def login(self,username,password):
        self.getEmailId_input().send_keys(username)
        self.getPassword_input().send_keys(password)
        self.getSignIn_button().click()


