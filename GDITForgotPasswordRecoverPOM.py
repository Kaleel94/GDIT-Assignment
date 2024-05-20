from selenium import webdriver
from selenium.webdriver.common.by import By

class PasswordRecoveryPage:
        #elementLocators
    txtbox_forgot_email_id="Email"
    button_forgot_username_linktext="Forgot username?"
    button_fp_send_email_xpath="xpath_html_send_email_example"

    #constrcutors
    def __init__(self,driver):
        self.driver = driver
    #actionMethods
    def setForgotEmail(self,email):
        forgot_email_txt= self.driver.find_element(By.ID,self.txtbox_forgot_email_id)
        forgot_email_txt.clear()
        forgot_email_txt.send_keys(email)

    def clickForgotUsername(self):
        self.driver.find_element(By.LINK_TEXT,self.button_forgot_username_linktext).click()
        return UserNameRecoveryPage #Assume in mind that UserNameRecoveryPage class exists

    def clickSendEmail(self):
        self.driver.find_element(By.XPATH,self.button_fp_send_email_xpath).click()