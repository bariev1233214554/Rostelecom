import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pytest

def test_successful_vphn(browser, credentials):
    ''' Функция для проверки восстановления пароля по телефону. Берет данные из фаила .eve.
        Изменяя данные в файле (есть готовые шаблоны) можно провести как позитивные, так и негативные тесты.
        Тест успешен в случае авторизации по новому паролю.
        '''
    wait = WebDriverWait(browser, 60)
    # Берем данные из фикстуры
    phone = credentials["phone"]
    password = credentials["password"]
    browser.get("https://b2c.passport.rt.ru/")


    # Кликаем по вкладке забыли пароль
    klic_input = wait.until(EC.visibility_of_element_located((By.ID, "forgot_password")))
    klic_input.click()

    # Кликаем по вкладке Телефон
    klic_input = wait.until(EC.visibility_of_element_located((By.ID, "t-btn-tab-phone")))
    klic_input.click()

    # Ввод телефона
    phone_input = wait.until(EC.visibility_of_element_located((By.ID, "username")))
    phone_input.clear()
    phone_input.send_keys(phone)

    #Вводим проверочный код и нажимаеи продолжить

    # Ввыбрать телефон если телефон пустой в фаиле .env - емаил

    phonev_input = wait.until(EC.visibility_of_element_located((By.ID, "sms-reset-type")))
    phonev_input.click()
    print("ВВеден Email.")
    time.sleep(2)

    continue_button_secondary = wait.until(EC.visibility_of_element_located((By.ID, "reset-form-submit")))
    continue_button_secondary.click()

    # Ввод пароля
    password_input = wait.until(EC.visibility_of_element_located((By.ID, "password-new")))
    password_input.clear()
    password_input.send_keys(password)

    passwordnew_input = wait.until(EC.visibility_of_element_located((By.ID, "password-confirm")))
    passwordnew_input.clear()
    passwordnew_input.send_keys(password)

    passwordnew_input = wait.until(EC.visibility_of_element_located((By.ID, "t-btn-reset-pass")))
    passwordnew_input.click()

    #Проверка, что пароль поменялся

    # Кликаем по вкладке Телефон
    klic_input = wait.until(EC.visibility_of_element_located((By.ID, "t-btn-tab-phone")))
    klic_input.click()

    # Ввод телефона
    phone_input = wait.until(EC.visibility_of_element_located((By.ID, "username")))
    phone_input.clear()
    phone_input.send_keys(phone)

    # Ввод пароля
    password_input = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    password_input.clear()
    password_input.send_keys(password)

    login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    login_button.click()

    # Проверка на ошибку входа
    error_selector = ".error-message, .form-error, [role='alert'], span.error"
    try:
        error_element = browser.find_element(By.CSS_SELECTOR, error_selector)
        if error_element.is_displayed():
            pytest.fail(f"Авторизация не удалась: {error_element.text}")
    except NoSuchElementException:
        pass

    # Ждем кнопку ЛК
    lk_button = wait.until(EC.visibility_of_element_located((By.ID, "lk-btn")))
    assert lk_button.is_displayed()
    print("Тест пройден!")




