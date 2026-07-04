from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_successful_login(browser, credentials):
    ''' Функция для проверки авторизации по кнопки VK.
    Для теста нужно устройство с установленным приложением Vk. Сканер qr должен быть открыт.
        '''
    wait = WebDriverWait(browser, 30)
    phone = credentials["phone"]
    password = credentials["password"]


    # Берем данные из фикстуры
    browser.get("https://b2c.passport.rt.ru/")

    # Кликаем по кнопке OK
    klic_input = wait.until(EC.visibility_of_element_located((By.ID, "oidc_ok")))
    klic_input.click()

    phone_input = wait.until(EC.visibility_of_element_located((By.ID, "field_email")))
    phone_input.clear()
    phone_input.send_keys(phone)

     #Ввод пароля
    password_input = wait.until(EC.visibility_of_element_located((By.ID, "field_password")))
    password_input.clear()
    password_input.send_keys(password)

    btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#widget-el input[type='submit']")))
    btn.click()


    # Ждем кнопку ЛК
    lk_button = wait.until(EC.visibility_of_element_located((By.ID, "lk-btn")))
    assert lk_button.is_displayed()
    print("Тест пройден!")



