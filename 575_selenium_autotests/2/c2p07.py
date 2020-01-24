from selenium import webdriver
import os


if __name__ == "__main__":
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 

    driver = webdriver.Chrome()
    url = "http://suninjuly.github.io/file_input.html"
    driver.get(url)

    driver.find_element_by_name("firstname").send_keys("firstname")
    driver.find_element_by_name("lastname").send_keys("lastname")
    driver.find_element_by_name("email").send_keys("email")
    driver.find_element_by_id("file").send_keys(file_path)
    driver.find_element_by_tag_name("button").click()
    