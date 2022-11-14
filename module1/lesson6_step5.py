import math
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
try:
    page = 'http://suninjuly.github.io/find_link_text'
    text = str(math.ceil(math.pow(math.pi, math.e)*10000))
    browser.get(page)
    link = browser.find_element(By.LINK_TEXT, text)
    link.click()

    first_name = browser.find_element(By.NAME, 'first_name')
    first_name.send_keys('Dzianis')

    last_name = browser.find_element(By.NAME, 'last_name')
    last_name.send_keys('Palkhouski')

    city = browser.find_element(By.CLASS_NAME, 'city')
    city.send_keys('Gantsevichi')

    country = browser.find_element(By.ID, 'country')
    country.send_keys('Belarus')

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
finally:
    time.sleep(7)
    browser.quit()
