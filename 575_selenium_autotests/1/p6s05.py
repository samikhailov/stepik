from selenium import webdriver
import math
from time import sleep
from s04 import fill_fields


link = "http://suninjuly.github.io/find_link_text"

browser = webdriver.Chrome()
browser.get(link)
browser.find_element_by_partial_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000))).click()
fill_fields(browser)
sleep(30)
browser.quit()