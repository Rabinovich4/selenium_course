import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    continue_link = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    continue_link.click()
    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys('Petrov')
    input3 = browser.find_element(By.CLASS_NAME, 'city')
    input3.send_keys('Smolensk')
    input4 = browser.find_element(By.ID, 'country')
    input4.send_keys('Rusia')
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()


finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла