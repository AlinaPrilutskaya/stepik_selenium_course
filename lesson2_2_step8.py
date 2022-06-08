from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'some_file')           # добавляем к этому пути имя файла

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector('[placeholder="Enter first name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector('[placeholder="Enter last name"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector('[placeholder="Enter email"]')
    input3.send_keys("some@mail.ru")
    element = browser.find_element_by_css_selector("[type='file']")


    element.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()