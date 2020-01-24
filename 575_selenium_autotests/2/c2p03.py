from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math


if __name__ == "__main__":
    url = "http://suninjuly.github.io/selects1.html"

    browser = webdriver.Chrome()
    browser.get(url)

    num1 = browser.find_element_by_id("num1")
    num2 = browser.find_element_by_id("num2")
    sum = int(num1.text) + int(num2.text)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(sum))
    browser.find_element_by_tag_name("button").click()

    input()
    browser.quit()
