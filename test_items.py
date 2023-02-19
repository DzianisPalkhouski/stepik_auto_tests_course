import time
from selenium.webdriver.common.by import By


def test_product_page_has_add_to_basket_button(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(5)
    assert browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')
