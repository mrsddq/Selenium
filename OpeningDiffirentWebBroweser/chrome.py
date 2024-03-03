from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.google.com/')
driver.maximize_window()
sleep(10)

driver.close()
# The quit() method closes the entire browser and terminates the WebDriver session. It closes all open browser windows and releases the associated memory and resources. On the other hand, the close() method is used to close the current browser window or tab while keeping the WebDriver session active.9 Jul 2023
