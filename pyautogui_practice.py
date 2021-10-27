import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://apollo-qa.rvaed.dev/login')
driver.maximize_window()

username = driver.find_element_by_id('username')
password = driver.find_element_by_id('password')

username.click()
username.send_keys('superadmin@rtslabs.com')

password.click()
password.send_keys('eY6Squequg2GF#')
password.send_keys(Keys.ENTER)

time.sleep(1)

driver.get('https://apollo-qa.rvaed.dev/clients/361bcd0f-9009-494b-890d-feb11d78aa5b/campaigns/1a71ead9-9754-4667-a934-656745410c91/creative/a59a9ace-3cc4-468e-8df0-d52592d82b8b/versions/82327018-e4b3-491c-b23b-efb780282672/email-builder/preview')
time.sleep(1)

pyautogui.moveTo(1100, 430)
pyautogui.click()
#driver.find_elements_by_css_selector('#root > div > main > article > div > div > div.css-5pwjfz > main > article > div > div > div.css-12v2k1n > div > label:nth-child(1)')

time.sleep(1)

#im = pyautogui.screenshot()
#if im.getpixel((360, 480)) == (255, 0, 0):
    #print("yes")

im = pyautogui.screenshot()
print(im.getpixel((360, 400)))

#Below is the function to make sure a coordinate matches a certain color
if pyautogui.pixelMatchesColor(360, 480, (255, 0, 0)):
    print('yes')
else:
    print('no')

#pyautogui.typewrite('C:\Users\siddeeqahfichman\Downloads\Arrow-circle-down-svgrepo-com')
#pyautogui.press('enter')
