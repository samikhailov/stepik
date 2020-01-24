from selenium import webdriver
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


if __name__ == "__main__":
    url = "http://suninjuly.github.io/execute_script.html"

    browser = webdriver.Chrome()
    browser.get(url)

    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("window.scrollBy(0, 120);", button)
    browser.find_element_by_id("answer").send_keys(y)
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()

    button.click()

    input()
    browser.quit()
