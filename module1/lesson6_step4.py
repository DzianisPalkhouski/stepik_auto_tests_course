import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
try:
    # link = 'http://suninjuly.github.io/simple_form_find_task.html'
    link = 'http://suninjuly.github.io/find_xpath_form'
    browser.get(link)

    first_name = browser.find_element(By.NAME, 'first_name')
    first_name.send_keys('Dzianis')

    last_name = browser.find_element(By.NAME, 'last_name')
    last_name.send_keys('Palkhouski')

    city = browser.find_element(By.CLASS_NAME, 'city')
    city.send_keys('Gantsevichi')

    country = browser.find_element(By.ID, 'country')
    country.send_keys('Belarus')

    # button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button = browser.find_element(By.XPATH, '//form/div[6]/button[3]')
    button.click()
finally:
    time.sleep(10)
    browser.quit()
