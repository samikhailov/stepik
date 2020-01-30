# coding=utf-8

import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


links = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
]
@pytest.mark.parametrize('link', links)
def test_reg1(browser, link):
    browser.get(link)
    answer = math.log(int(time.time()))
    textarea = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.TAG_NAME, "textarea")))
    textarea.send_keys(str(answer))
    browser.find_element_by_class_name('submit-submission').click()
    messsage = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "pre.smart-hints__hint"))).text
    assert messsage == "Correct!", 'The message doesn\'t match with reference.'
