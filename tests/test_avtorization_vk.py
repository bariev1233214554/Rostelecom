from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_successful_vk(browser, credentials):
    ''' Функция для проверки авторизации по кнопки VK.
    Для теста нужно устройство с установленным приложением Vk. Сканер qr должен быть открыт.
        '''
    wait = WebDriverWait(browser, 120)
    # Берем данные из фикстуры
    browser.get("https://b2c.passport.rt.ru/")

    # Кликаем по кнопке VK
    klic_input = wait.until(EC.visibility_of_element_located((By.ID, "oidc_vk")))
    klic_input.click()

    #Сканируем Qr код и вводим код из цифр.

    # Ждем кнопку ЛК
    lk_button = wait.until(EC.visibility_of_element_located((By.ID, "lk-btn")))
    assert lk_button.is_displayed()
    print("Тест пройден!")



