import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def test_successful_tinkoff(browser, credentials):
    ''' Функция для проверки авторизации по кнопки Тинькофф. Для теста должен иметься доступ к мобильному телефону для получения и введения смс.
        '''
    wait = WebDriverWait(browser, 120)
    # Берем данные из фикстуры
    phone = credentials["phone"]
    browser.get("https://b2c.passport.rt.ru/")

    # Кликаем по кнопке Тинькофф
    klic_input = wait.until(EC.visibility_of_element_located((By.ID, "oidc_tinkoff")))
    klic_input.click()

    # ВВодим телефон и ждем смс
    phone_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[automation-id='phone-input']")))
    phone_input.clear()
    phone_input.send_keys(phone)
    time.sleep(1)
    phone_input.send_keys(Keys.ENTER)

    #ВВодим смс вручную

    # Ждем кнопку ЛК
    lk_button = wait.until(EC.visibility_of_element_located((By.ID, "lk-btn")))
    assert lk_button.is_displayed()
    print("Тест пройден!")



