from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_successful_mail(browser, credentials):
    ''' Функция для проверки авторизации по кнопки mail.
        '''
    wait = WebDriverWait(browser, 3000)
    # Берем данные из фикстуры
    email = credentials["email"]
    password = credentials["password"]
    browser.get("https://b2c.passport.rt.ru/")

    # Кликаем по кнопке mail
    klic_input = wait.until(EC.visibility_of_element_located((By.ID, "oidc_mail")))
    klic_input.click()

    # Ввод Емаил
    email_input = wait.until(EC.visibility_of_element_located((By.ID, "login")))
    email_input.clear()
    email_input.send_keys(email)

    # Ввод пароля
    password_input = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    password_input.clear()
    password_input.send_keys(password)

    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#login-form > div.login-form__footer > button")))
    button.click()


    # Ждем кнопку ЛК
    lk_button = wait.until(EC.visibility_of_element_located((By.ID, "lk-btn")))
    assert lk_button.is_displayed()
    print("Тест пройден!")



