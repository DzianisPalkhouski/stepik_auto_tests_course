import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
try:
    link = 'http://suninjuly.github.io/registration1.html'
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, '.first[placeholder="Input your first name"]').send_keys('Dzianis')
    browser.find_element(By.CSS_SELECTOR, '.second[placeholder="Input your last name"]').send_keys('Palkhouski')
    browser.find_element(By.CLASS_NAME, 'third').send_keys('denvereal91@gmail.com')

    browser.find_element(By.CLASS_NAME, 'btn').click()
    time.sleep(1)

    welcome_text = browser.find_element(By.TAG_NAME, 'h1').text
    assert welcome_text == 'Congratulations! You have successfully registered!'
finally:
    time.sleep(3)
    browser.quit()
