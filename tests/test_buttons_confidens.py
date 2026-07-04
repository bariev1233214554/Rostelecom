import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_successful_conf(browser, credentials):
    ''' Функция для проверки кнопки Политикой конфиденциальности .
        '''
    browser.get("https://b2c.passport.rt.ru/")
    wait = WebDriverWait(browser, 15)
    old_url = browser.current_url

    #Нажимаем кнопку Политикой конфиденциальности
    lic_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Политикой конфиденциальности')]"))
    )
    lic_button.click()

    #Кнопка открыват страницу с Политикой конфиденциальности
    time.sleep(2)
    wait.until(lambda driver: driver.current_url != old_url)
    print(f"Кнопка  работает (URL изменился)")
















