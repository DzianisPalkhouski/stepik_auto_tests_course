import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, 'input:nth-child(2)').send_keys('Kanye')
    browser.find_element(By.CSS_SELECTOR, 'input:nth-child(4)').send_keys('West')
    browser.find_element(By.CSS_SELECTOR, 'input:nth-child(6)').send_keys('bipolar@gmail.com')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'ye.txt')
    browser.find_element(By.ID, 'file').send_keys(file_path)
    browser.find_element(By.TAG_NAME, 'button').click()
finally:
    time.sleep(5)
    browser.quit()
