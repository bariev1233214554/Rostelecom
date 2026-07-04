import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def test_successful_login(browser, credentials):
    ''' Функция для проверки  Пользовательским соглашением в подвале сайта.
        '''
    browser.get("https://b2c.passport.rt.ru/")
    wait = WebDriverWait(browser, 15)
    old_url = browser.current_url

    #Нажимаем кнопку с  Пользовательским соглашением в подвале сайта

    klic_input = wait.until(EC.visibility_of_element_located((By.ID, "rt-auth-agreement-link")))
    klic_input.click()
    time.sleep(1)
    wait.until(lambda driver: driver.current_url != old_url)
    print(f"Кнопка  работает (URL изменился)")
















