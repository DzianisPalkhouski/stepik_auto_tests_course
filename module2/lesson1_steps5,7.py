import time
import math
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def calc(num):
    return str(math.log(abs(12 * math.sin(int(num)))))


browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# link = 'https://suninjuly.github.io/math.html'
link = 'http://suninjuly.github.io/get_attribute.html'
browser.get(link)
# x_element = browser.find_element(By.ID, 'input_value')
x = browser.find_element(By.TAG_NAME, 'img').get_attribute('valuex')
# x = x_element.text
y = calc(x)
browser.find_element(By.CSS_SELECTOR, '#answer[required]').send_keys(y)
# browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]').click()
browser.find_element(By.ID, 'robotCheckbox').click()
browser.find_element(By.ID, 'robotsRule').click()
browser.find_element(By.CLASS_NAME, 'btn-default').click()
time.sleep(5)
browser.quit()
