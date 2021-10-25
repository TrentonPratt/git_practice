import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://apollo-qa.rvaed.dev/login')

username = driver.find_element_by_id('username')
password = driver.find_element_by_id('password')

username.click()
username.send_keys('superadmin@rtslabs.com')

password.click()
password.send_keys('eY6Squequg2GF#')
password.send_keys(Keys.ENTER)

time.sleep(1)

driver.get('https://apollo-qa.rvaed.dev/clients/922f8541-3859-4ae4-8b21-c563a5ab9132/settings/themes/a4f0c2b2-b69d-42e6-944d-77103eb6ed55/theme-builder/a4f0c2b2-b69d-42e6-944d-77103eb6ed55/logos')

time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div/main/article/div/div/div/main/aside/div/div[1]/div/div[1]/div[1]/div/div/a').click()

time.sleep(1)

pyautogui.typewrite('C:\Users\siddeeqahfichman\Downloads\Arrow-circle-down-svgrepo-com')
pyautogui.press('enter')
