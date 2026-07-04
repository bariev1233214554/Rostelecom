import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_successful_popd(browser, credentials):
    ''' Функция для проверки кнопки Политикой обработки персональных данных .
        '''
    browser.get("https://b2c.passport.rt.ru/")
    wait = WebDriverWait(browser, 15)
    old_url = browser.current_url

    #Нажимаем кнопку с Политикой обработки персональных данных
    klic_input = wait.until(EC.visibility_of_element_located((By.ID, "rt-auth-pdn-link")))
    klic_input.click()
    time.sleep(1)
    wait.until(lambda driver: driver.current_url != old_url)
    print(f"Кнопка  работает (URL изменился)")
















