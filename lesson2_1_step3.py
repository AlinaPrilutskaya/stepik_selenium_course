from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)

    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()


    radio = browser.find_element_by_css_selector("[for='robotsRule']")
    radio.click()

    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()