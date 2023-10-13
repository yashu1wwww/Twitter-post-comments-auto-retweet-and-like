from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import random


driver= webdriver.Chrome()
driver.maximize_window()

driver.get("https://twitter.com/i/flow/login")
time.sleep(4)
email = driver.find_element_by_name('text')
email.send_keys("tweety") #replace with your twitter username
email.send_keys(Keys.ENTER)
time.sleep(3)
password = driver.find_element_by_name("password")
password.send_keys("tweet122@#$!") #replace with your twitter password
password.send_keys(Keys.ENTER)
time.sleep(5)
driver.get("https://twitter.com/X/status/1712533971194527917") #Which account's posts do you want to comment on, retweet, and like

# Wait for the search results to load
time.sleep(4)

#It will automatically retweet and like all comments on the post until you stop.

while True:
    try:
        retweet_button = driver.find_element_by_xpath("//div[@data-testid='retweet']/div").click() #retweet button
        time.sleep(1)
        
        retweet_button = driver.find_element_by_xpath("//div[@data-testid='retweetConfirm']/div").click() #retweet click #confirm
        time.sleep(1)
        
        like_button = driver.find_element_by_xpath("//div[@data-testid='like']/div") #like button
        like_button.click()
        
        time.sleep(1) 
    except NoSuchElementException:
        break  