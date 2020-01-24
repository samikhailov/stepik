import os

from selenium import webdriver


if __name__ == "__main__":
    driver = webdriver.Chrome()
    url = "http://suninjuly.github.io/cats.html"
    driver.get(url)

    driver.find_element_by_id("button")

    input()
    driver.quit()
