import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_successful_sogl(browser, credentials):
    ''' Функция для проверки кнопки c Пользовательским соглашением.
        '''
    browser.get("https://b2c.passport.rt.ru/")
    wait = WebDriverWait(browser, 15)
    old_url = browser.current_url
# нажимаем на кнопку пользовательского соглашения
    lic_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Пользовательским соглашением')]"))
    )
    lic_button.click()

    time.sleep(2)
    wait.until(lambda driver: driver.current_url != old_url)
    print(f"Кнопка  работает (URL изменился)")
















