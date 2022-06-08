from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select



link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()

    browser.get(link)

    x = int(browser.find_element_by_id("num1").text)
    y = int(browser.find_element_by_id("num2").text)
    sum = str(x + y)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum)  # ищем элемент с текстом "Python"

    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()