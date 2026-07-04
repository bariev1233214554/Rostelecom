import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def test_successful_ya(browser, credentials):
    ''' Функция для проверки авторизации по кнопки Яндекс.
    Для теста должен имется доступ к Яндекс id для получения и введения кода
        '''
    wait = WebDriverWait(browser, 120)
    # Берем данные из фикстуры
    phone = credentials["phone"]
    browser.get("https://b2c.passport.rt.ru/")

    # Кликаем по кнопке Яндекс
    klic_input = wait.until(EC.visibility_of_element_located((By.ID, "oidc_ya")))
    klic_input.click()

    phone_input = wait.until(EC.visibility_of_element_located((By.ID, "react-aria-«Rm6b»")))
    phone_input.clear()
    phone_input.send_keys(phone)
    time.sleep(1)
    phone_input.send_keys(Keys.ENTER)
    time.sleep(2)

    # ВВодим смс вручную

    # Нажимаем карточку аккаунта
    first_card = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".AccountSuggestList-card-wrapper")))
    first_card.click()

    # Нажимаем кнопку пропустить и входим в лк
    btn_later = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='webauthn-reg-later-button']")))
    btn_later.click()


    # Ждем кнопку ЛК
    lk_button = wait.until(EC.visibility_of_element_located((By.ID, "lk-btn")))
    assert lk_button.is_displayed()
    print("Тест пройден!")



