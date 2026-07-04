import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_successful_login(browser, credentials):
    ''' Функция для проверки кнопки связи.
        '''
    browser.get("https://b2c.passport.rt.ru/")
    wait = WebDriverWait(browser, 15)

    #Нажимаем кнопку 88001000800
    phone_link = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.rt-footer-right__support-contact"))
    )
    phone_link.click()
    time.sleep(1)



















