import os
import math

from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


if __name__ == "__main__":
    driver = webdriver.Chrome()
    url = "http://suninjuly.github.io/alert_accept.html"
    driver.get(url)

    driver.find_element_by_tag_name("button").click()
    confirm = driver.switch_to_alert()
    confirm.accept()

    x_element = driver.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    driver.find_element_by_id("answer").send_keys(y)
    driver.find_element_by_tag_name("button").click()

    input()
    driver.quit()
