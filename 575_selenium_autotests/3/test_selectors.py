# coding=utf-8

import unittest
from selenium import webdriver
import time


class TestSelectors(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Заполнение обязательных полей
        first = browser.find_element_by_css_selector("div.first_block input.first")
        first.send_keys("Ivan")
        second = browser.find_element_by_css_selector("div.first_block input.second")
        second.send_keys("Petrov")
        third = browser.find_element_by_css_selector("div.first_block input.third")
        third.send_keys("Smolensk@Smolensk.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться, ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")

        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                            "Should be absolute value of a number")

    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Заполнение обязательных полей
        first = browser.find_element_by_css_selector("div.first_block input.first")
        first.send_keys("Ivan")
        second = browser.find_element_by_css_selector("div.first_block input.second")
        second.send_keys("Petrov")
        third = browser.find_element_by_css_selector("div.first_block input.third")
        third.send_keys("Smolensk@Smolensk.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться, ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")

        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                            "Should be absolute value of a number")

if __name__ == "__main__":
    unittest.main()






