# Bots-Project
In this repo we are making different types of bots that could be implemented in various different projects as standalones.

# AutoLoginBot
"Web Scraping and Automated Login using Selenium and Firefox WebDriver"

-> This Python script demonstrates how to automate the login process on a website using the Selenium library with the Firefox WebDriver. It also includes a delay   before clicking the login button.

**Prerequisites**

Python

Mozilla Firefox

Selenium 
->  pip install selenium

WebDriver Manager 
->  pip install webdriver_manager

**Configuration**

Replace "your_username_here" and "your_password_here" with your actual login credentials.
Update "useriid", "actlpass", and "psslogin" with the HTML element IDs of the corresponding fields and submit button on the website you are automating.

**Features**

->Initializes a Firefox WebDriver using WebDriver Manager.

->Navigates to the specified website.

->Fills in the username and password fields.

->Introduces a delay (adjustable) before clicking the login button.

->Clicks the login button.

->You can add further automation steps after successful login.
