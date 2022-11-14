import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
link = 'http://suninjuly.github.io/selects2.html'
browser.get(link)
first_num = browser.find_element(By.ID, 'num1').text
second_num = browser.find_element(By.ID, 'num2').text
total = int(first_num) + int(second_num)
dropdown = Select(browser.find_element(By.CLASS_NAME, 'custom-select'))
dropdown.select_by_value(str(total))
browser.find_element(By.CLASS_NAME, 'btn').click()
time.sleep(10)
browser.quit()
