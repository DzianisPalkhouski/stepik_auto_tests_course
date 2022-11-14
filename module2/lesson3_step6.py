import math
import pyperclip
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def calc(num):
    return str(math.log(abs(12 * math.sin(int(num)))))


browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
link = 'http://suninjuly.github.io/redirect_accept.html'
browser.get(link)
browser.find_element(By.TAG_NAME, 'button').click()
windows = browser.window_handles  # list with the names of the tabs
browser.switch_to.window(windows[1])
result = calc(browser.find_element(By.ID, 'input_value').text)
browser.find_element(By.ID, 'answer').send_keys(result)
button = browser.find_element(By.TAG_NAME, 'button')
button.click()
answer = browser.switch_to.alert.text.split(': ')[-1]
pyperclip.copy(answer)  # copying the answer to the clipboard
browser.quit()
