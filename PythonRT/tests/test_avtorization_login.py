from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pytest

def test_successful_login(browser, credentials):
    ''' Функция для проверки авторизации по Логину. Берет Логин и пароль из фаила .eve.
        Изменяя Логин и пароль в файле (есть готовые шаблоны)
        можно провести как позитивные, так и негативные тесты. '''
    wait = WebDriverWait(browser, 15)
    # Берем данные из фикстуры
    login = credentials["login"]
    password = credentials["password"]
    browser.get("https://b2c.passport.rt.ru/")

    # Кликаем по вкладке Логин
    klic_input = wait.until(EC.visibility_of_element_located((By.ID, "t-btn-tab-login")))
    klic_input.click()

    # Ввод Логин
    login_input = wait.until(EC.visibility_of_element_located((By.ID, "username")))
    login_input.clear()
    login_input.send_keys(login)

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



