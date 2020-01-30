from selenium import webdriver
import time 


def fill_fields(browser):
    value1 = 'input[name="first_name"]'
    value2 = 'last_name'
    value3 = 'city'
    value4 = 'country'

    input1 = browser.find_element_by_tag_name(value1)
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name(value2)
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name(value3)
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id(value4)
    input4.send_keys("Russia")



if __name__ == "__main__":
    url = "http://suninjuly.github.io/simple_form_find_task.html"

    try:
        browser = webdriver.Chrome()
        browser.get(url)
        fill_fields(browser)
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()
