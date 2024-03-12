from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import random

randomization = random.randint(1, 10000)
print(randomization)

driver = webdriver.Chrome()
driver.get('https://scorecount.com/click-counter/')
driver.maximize_window()

# mouse
clicking = driver.find_element(By.XPATH,'//*[@id="counter1"]/div[3]')
randomOfRandom=random.randint(1, randomization)
print(randomOfRandom)
for _ in range(randomOfRandom):
    clicking.click()
    sleep(1)
driver.get('https://clickcounter.io/keyboard-counter')
driver.maximize_window()


# keyboard
randomOfRandomOfRandom=random.randint(1, randomOfRandom)
print(randomOfRandomOfRandom)
typing = driver.find_element(By.XPATH,'/html/body')
alphabets = 'abcdefghijklmnopqrstuvwxyz'
keywords = ''.join([alphabets[i % len(alphabets)] for i in range(randomOfRandomOfRandom)])
typing.send_keys(keywords)

# Close the browser after 5 seconds
sleep(5)
