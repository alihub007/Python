from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

with webdriver.Safari() as driver:
    driver.get('https://www.facebook.com')
    sleep(2)
    userbox = driver.find_element_by_xpath('//*[@id="email"]')
    userbox.send_keys('user_name')
    passbox = driver.find_element_by_xpath('//*[@id="pass"]')
    passbox.send_keys('Password')
    passbox.send_keys(Keys.ENTER)
    sleep(5)
