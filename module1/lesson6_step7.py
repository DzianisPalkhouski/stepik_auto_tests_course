import time
import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
symbols = string.ascii_letters + string.digits
try:
    link = 'http://suninjuly.github.io/huge_form.html'
    browser.get(link)

    elements = browser.find_elements(By.TAG_NAME, 'input')
    for element in elements:
        element.send_keys(''.join(random.choice(symbols) for i in range(10)))
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

finally:
    time.sleep(7)
    browser.quit()
