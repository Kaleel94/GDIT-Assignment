# GDIT-Assignment
Files addressing the assignment prompt for GDIT

Read Me
-----------

1. **List the tests you would expect to perform on this page, along with the expected outcome of each test.**
   
The file for this question is TestPlan.txt
The file provides my list of test cases using Gherkin syntax as well as what is in scope and what is out of scope 


2. **Create pseudocode for automated tests you would use to exercise this functionality. Assume the test runner/framework of your choice is a given, but create a test file and any backing files you feel would be necessary for these tests. Understanding that you don’t have access to the HTML for these pages, please include information on how you would expect to locate the controls needed for the test, including any possible variations you would expect based on the screenshots**.
   
The files are:
-PseudoCode.txt 
-GDITLoginPagePOM.py 
-GDITForgotPasswordRecoverPOM.py

PseudCode.txt provides PseudoCode of my automated tests in correlation with the test cases I provided in TestPlan.txt
Also included are "backing files" such as the GDITLoginPagePOM.py file and GDITForgotPasswordRecoverPOM.py (rough code in python using Selenium)

Information used to locate the controls needed for the test:
1a) With the placeholder text in Email and Password you can infer that the HTML elements could have identifiers:
attributes ID or name attribute 
ex: id="username"

2a) With the email textbox being present in both Login and Forgot password, one can infer that HTML elements can select the email field using CSS selector and tag the ID or class name

3a) With the Sign In button being unique and quite distinct, you can infer this button could be located by its XPath if no ID identifier is present. 
if an ID attribute is present it could be id="submit" or id="login"

4a) You can use CSS selector to target a consistent class, if there are many dynamic changes, for example the email textbox (if it were to change)

5a) "Forgot Password?" is a hyperlink and likely linked with text as that is usually a common naming with frontend testing. You can use a locator such as BY. LINK_Text (in selenium this is what I use)

3. **Explain how you might integrate these tests into a larger test suite for the full application.**
You can integrate these automated tests into a larger test suite by grouping them by functionality. Example could be a fixture called Authentication. Login/PasswordRevcovery could be grouped with a logout/UsernameRecovery (assuming logout & Username Recovery are parts of a larger test suite). The easiest and most efficient way would be to integrate the tests into a CI/CD pipeline for automated execution. I have used Bamboo and Jenkins for this, and it's great because tests are automatically ran when new automated code is checked in.You can also set up smoke tests and regression tests to run a specific time/occurrence a day. This is key because it allows you to catch issues and bugs early from these tests being ran throughout the day or code commits.
