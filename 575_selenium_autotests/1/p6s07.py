from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from time import sleep
from s04 import fill_fields


link = "http://suninjuly.github.io/find_xpath_form"

browser = webdriver.Chrome()
browser.get(link)
fill_fields(browser)
button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
button.click()
sleep(30)
browser.quit()
