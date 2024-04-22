import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def autologin(browser, website_link, username, password):
    browser.get(website_link)
    try:
        # Find and fill the username field using the HTML element ID
        username_element = browser.find_element(By.ID, "useriid")
        username_element.send_keys(username)

        # Find and fill the password field using the HTML element ID
        password_element = browser.find_element(By.ID, "actlpass")
        password_element.send_keys(password)

        # Introduce a delay (e.g., 3 seconds) before clicking the submit button
        time.sleep(2)

        # Find and click the submit button using the HTML element ID
        signInButton = browser.find_element(By.ID, "psslogin")
        signInButton.click()

        # Wait for the page to load (adjust the sleep duration as needed)
        time.sleep(2)
    except Exception as e:
        print("An error occurred during login:", e)

def handle_alert(browser):
    try:
        # Wait for the alert to appear
        alert = WebDriverWait(browser, 5).until(EC.alert_is_present())

        # Dismiss the alert by clicking OK
        alert.accept()
    except Exception as e:
        print("An error occurred while handling alert:", e)

def capture_assignment_tab(browser, num_screenshots=1):
    try:
        # Click on the assignment tab
        assignment_tab_xpath = "//img[contains(@src, 'assignments.svg')]"
        assignment_tab = browser.find_element(By.XPATH, assignment_tab_xpath)
        assignment_tab.click()

        # Wait for the page to load
        time.sleep(3)

        # Create a folder to store the screenshots
        folder_name = "screenshots_assignment"
        os.makedirs(folder_name, exist_ok=True)

        # Loop to capture multiple screenshots
        for i in range(1, num_screenshots + 1):
            # Define the screenshot file name with a unique identifier
            screenshot_filename = f"{folder_name}/screenshot_{i}.png"
            # Capture the screenshot and save it with the defined file name
            browser.save_screenshot(screenshot_filename)
    except Exception as e:
        print("An error occurred while capturing screenshots of the assignment tab:", e)

def capture_home_tab(browser):
    try:
        # Click on the home tab
        home_tab_xpath = "/html/body/div[1]/div[1]/div/div[3]/div[1]/div/ol/li[1]/a"
        home_tab = browser.find_element(By.XPATH, home_tab_xpath)
        home_tab.click()

        # Wait for the page to load
        time.sleep(3)

        # Handle alert if it appears
        handle_alert(browser)

        # Wait
        time.sleep(3)
    except Exception as e:
        print("An error occurred while navigating to the home tab:", e)

def capture_attendance_tab(browser, num_screenshots=1):
    try:
        # Click on the attendance tab
        attendance_tab_xpath = "//img[contains(@src, 'attendance.svg')]"
        attendance_tab = browser.find_element(By.XPATH, attendance_tab_xpath)
        attendance_tab.click()

        # Wait for the page to load
        time.sleep(3)

        # Create a folder to store the screenshots
        folder_name = "screenshots_attendance"
        os.makedirs(folder_name, exist_ok=True)

        # Loop to capture multiple screenshots
        for i in range(1, num_screenshots + 1):
            # Define the screenshot file name with a unique identifier
            screenshot_filename = f"{folder_name}/screenshot_{i}.png"
            # Capture the screenshot and save it with the defined file name
            browser.save_screenshot(screenshot_filename)
    except Exception as e:
        print("An error occurred while capturing screenshots of the attendance tab:", e)

if __name__ == "__main__":
    # Define your website link, username, and password
    website_link = "https://mrei.icloudems.com/corecampus/index.php"
    username = "12104005N094"
    password = "9560252503"

    # Initialize the WebDriver using GeckoDriverManager (no need for executable_path)
    browser = webdriver.Firefox()

    # Auto-login
    autologin(browser, website_link, username, password)

    # Capture screenshots of the assignment tab
    capture_assignment_tab(browser)

    # Navigate to the home tab and wait for 5 minutes
    capture_home_tab(browser)

    # Capture screenshots of the attendance tab
    capture_attendance_tab(browser)

    # Optionally, you can add more functionality or call other tabs.
    # To quit the browser, uncomment the following line:
    # browser.quit()
