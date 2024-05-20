from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
        #elementLocators
    txtbox_email_id="Email"
    txtbox_password_id="Password"
    button_signin_xpath="xpath_html_example"
    button_forgot_password_linktext="Forgot password?"


        #constructor
    def __init__(self, driver):
        self.driver=driver

        #action Methods


    def setEmail(self,email):
        usernametxt_box=self.driver.find_element(By.ID,self.txtbox_username_id)
        usernametxt_box.clear()
        usernametxt_box.send_keys(email)

    def setPassword(self,pwd):
        pwdtxt_box=self.driver.find_element(By.ID,self.txtbox_password_id)
        pwdtxt_box.clear()
        pwdtxt_box.send_keys(pwd)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_signin_xpath).click()
        return GDITHomePage #Assume in mind that a HomePage class was created

    def clickForgotPassword(self):
        self.driver.find_element(By.LINK_TEXT,self.button_forgot_password_linktext).click()
        return PasswordRecoveryPage #Assume in mind that a Password Recovery page is created
