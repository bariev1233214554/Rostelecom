import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys



def tst_tabulation( browser,znacenie,Xp):
    ''' Вспомогательная функция: Очищает строку логина и водит извлеченные из фаЙла .env значения.
    После сравнивает тип введеного значения с типом аутентификации.
           '''
    wait = WebDriverWait(browser, 15)
    one_input = wait.until(EC.element_to_be_clickable((By.ID, "username")))
    one_input.click()

    # Выделяем всё и удаляем
    one_input.send_keys(Keys.CONTROL + "a")
    one_input.send_keys(Keys.DELETE)

    # Вводим значение
    one_input.send_keys(znacenie)

    #Кликаем на строку ввода пароля для срабатывания автотаба
    password_input = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    password_input.click()
    time.sleep(2)
    assert browser.find_element(By.XPATH, Xp).is_displayed()


def test_successful_tbl(browser, credentials):
    ''' Функция для проверки таба выбора аутентификации. Проверяет сразу все типы аутентификации.
        '''

    # Берем данные из фикстуры
    chet = credentials["chet"]
    email = credentials["email"]
    phone = credentials["phone"]
    login = credentials["login"]
    browser.get("https://b2c.passport.rt.ru/")

    #Проверяеv типы аутентификации

    tst_tabulation(browser,phone, "//span[contains(text(), 'Мобильный телефон')]")
    print("Тест Мобильный телефон: ОК ")
    tst_tabulation(browser, email, "//span[contains(text(), 'Электронная почта')]")
    print("Тест Электронная почта: ОК")
    tst_tabulation(browser,login, "//span[contains(text(), 'Логин')]")
    print("Тест Логин: ОК")
    tst_tabulation(browser,chet, "//span[contains(text(), 'Лицевой счёт')]")
    print("Тест Лицевой счёт: ОК")














