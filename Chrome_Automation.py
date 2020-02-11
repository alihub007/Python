from time import sleep
from selenium import webdriver

with  webdriver.Safari() as wd:
    wd.get('https://www.google.com')
    sleep(10)