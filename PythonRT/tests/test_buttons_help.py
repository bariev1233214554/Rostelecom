import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_successful_login(browser, credentials):
    ''' Функция для проверки кнопки помощи.
        '''
    browser.get("https://b2c.passport.rt.ru/")
    wait = WebDriverWait(browser, 15)

    #Нажимаем кнопку Помощь
    klic_input = wait.until(EC.visibility_of_element_located((By.ID, "faq-open")))
    klic_input.click()
    time.sleep(1)

    # Нажимаем кнопку Войти с Ростелеком ID
    klicpag_input = wait.until(EC.visibility_of_element_located((By.ID, "faq-close")))
    klicpag_input.click()
    time.sleep(1)


















