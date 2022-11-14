import math
import pyperclip
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def calc(num):
    return str(math.log(abs(12 * math.sin(int(num)))))


browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
link = 'http://suninjuly.github.io/alert_accept.html'
browser.get(link)
browser.find_element(By.CLASS_NAME, 'btn').click()
browser.switch_to.alert.accept()
x = browser.find_element(By.ID, 'input_value').text
result = calc(x)
browser.find_element(By.ID, 'answer').send_keys(result)
browser.find_element(By.TAG_NAME, 'button').click()
answer = browser.switch_to.alert.text.split(': ')[-1]
pyperclip.copy(answer)  # copying the answer to the clipboard
browser.quit()
