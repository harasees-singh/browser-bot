from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# This version of ChromeDriver only supports Chrome version 104
# Current browser version is 104.0.5112.102
usernameStr = '{your username}'
passwordStr = '{your password}'

browser = webdriver.Chrome(executable_path = r"path_to_chrome_driver\chromedriver.exe")
browser.get(('http://172.31.1.203:8090/httpclient.html'))

# id for username input : username
# id for password input : password
username = browser.find_element(By.ID, 'username')
username.send_keys(usernameStr)
# fill the username
password = browser.find_element(By.ID, 'password')
password.send_keys(passwordStr)
# fill the password

nextButton = browser.find_element(By.ID, 'loginbutton')
nextButton.click() 
# click click 