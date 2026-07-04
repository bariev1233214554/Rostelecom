import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pytest

def test_successful_vch(browser, credentials):
    ''' Функция для проверки восстановления пароля по счету. Берет данные из фаила .eve.
        Изменяя тданные в файле (есть готовые шаблоны) можно провести как позитивные, так и негативные тесты.
        Тест успешен в случае авторизации по новому паролю.
        Выбор метода восстановления зависит от значения параметра TEST_PHONE в файле .env если телефон пустой - емаил '''
    wait = WebDriverWait(browser, 60)
    # Берем данные из фикстуры
    phone = credentials["phone"]
    password = credentials["password"]
    chet = credentials["chet"]
    browser.get("https://b2c.passport.rt.ru/")


    # Кликаем по вкладке забыли пароль
    klic_input = wait.until(EC.visibility_of_element_located((By.ID, "forgot_password")))
    klic_input.click()

    # Кликаем по вкладке Лицевой счет
    klic_input = wait.until(EC.visibility_of_element_located((By.ID, "t-btn-tab-ls")))
    klic_input.click()

    # Ввод Лицевой счет
    chet_input = wait.until(EC.visibility_of_element_located((By.ID, "username")))
    chet_input.clear()
    chet_input.send_keys(chet)

    #Вводим проверочный код и нажимаеи продолжить

    # Ввыбрать телефон если телефон пустой в файле .env - емаил

    if phone == "":
        phon_input = wait.until(EC.visibility_of_element_located((By.ID, "email-reset-type")))
        phon_input.click()
        print('Введен телефон')
    else:
        email_input = wait.until(EC.visibility_of_element_located((By.ID, "sms-reset-type")))
        email_input.click()
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

    # Кликаем по вкладке Лицевой счет
    klic_input = wait.until(EC.visibility_of_element_located((By.ID, "t-btn-tab-ls")))
    klic_input.click()

    # Ввод Лицевой счет
    chet_input = wait.until(EC.visibility_of_element_located((By.ID, "username")))
    chet_input.clear()
    chet_input.send_keys(chet)

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




