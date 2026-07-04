import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


def test_successful_login(browser, credentials):
    ''' Функция для проверки регистрации.  Берет данные для регистрации из фаила .eve.
        Изменяя данные в файле (есть готовые шаблоны)
        можно провести как позитивные, так и негативные тесты.
    PS с выбором региона не смок справиться - вставил костыль time.sleep
        '''
    wait = WebDriverWait(browser, 15)
    # Берем данные из фикстуры
    email = credentials["email"]
    password = credentials["password"]
    name = credentials["name"]
    family = credentials["family"]
    phone = credentials["phone"]
    region = credentials["region"]


    browser.get("https://b2c.passport.rt.ru/")

    # Нажать кнопку "Зарегистрироваться"
    registration_link = wait.until(
        EC.element_to_be_clickable((By.ID, "kc-register"))
    )
    registration_link.click()


    # Проверить переход на страницу регистрации
    expected_url_part = "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration"
    actual_url = browser.current_url
    assert expected_url_part in actual_url, f"Expected URL part: {expected_url_part}, Actual URL: {actual_url}"

    # Ввести имя
    name_input = browser.find_element(By.XPATH, "//input[@name='firstName']")
    name_input.clear()
    name_input.send_keys(name)

    # Ввести фамилию
    family_input = browser.find_element(By.XPATH, "//input[@name='lastName']")
    family_input.clear()
    family_input.send_keys(family)

    # Ввести регион вручную
    time.sleep(10)

    # Ввести email если емаил пустой - телефон
    email_input = browser.find_element(By.XPATH, "//input[@id='address']")
    email_input.send_keys(Keys.CONTROL + "a")
    email_input.send_keys(Keys.DELETE)
    email_input.send_keys(email)

    current_value = email_input.get_attribute("value")

    if not current_value or current_value.strip() == "":
        browser.execute_script(f"arguments[0].value = '{phone}';", email_input)
        browser.execute_script("""
                var el = arguments[0];
                el.dispatchEvent(new Event('input', { bubbles: true }));
                el.dispatchEvent(new Event('change', { bubbles: true }));
            """, email_input)
        print('Введен телефон')
    else:
        print("ВВеден Email.")

    password_input = wait.until(EC.element_to_be_clickable((By.ID, "password")))
    password_input.clear()
    password_input.send_keys(password)

    passw_input = wait.until(EC.element_to_be_clickable((By.ID, "password-confirm")))
    passw_input.clear()
    passw_input.send_keys(password)
    time.sleep(2)

    pagenex_input = browser.find_element(By.XPATH, "//button[@type='submit']")
    pagenex_input.click()

    #ВВод кода подтверждения
    time.sleep(30)

    lk_button = wait.until(EC.visibility_of_element_located((By.ID, "lk-btn")))
    assert lk_button.is_displayed()
    print("Тест пройден!")











