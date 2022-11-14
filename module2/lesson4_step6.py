import math
import pyperclip
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def calc(num):
    return str(math.log(abs(12 * math.sin(int(num)))))


browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
link = 'http://suninjuly.github.io/explicit_wait2.html'
browser.get(link)

WebDriverWait(browser, 12).until(ec.text_to_be_present_in_element((By.ID, 'price'), '$100'))
browser.find_element(By.ID, 'book').click()

browser.execute_script('window.scrollBy(0, 500);')
x = browser.find_element(By.ID, 'input_value').text
result = calc(x)
browser.find_element(By.ID, 'answer').send_keys(result)
browser.find_element(By.ID, 'solve').click()
WebDriverWait(browser, 12).until(ec.alert_is_present())

answer = browser.switch_to.alert.text.split(': ')[-1]
pyperclip.copy(answer)  # copying the answer to the clipboard
browser.quit()
