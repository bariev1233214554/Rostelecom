import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_successful_cook(browser, credentials):
    ''' Функция для проверки кнопки Cookies.
        '''
    browser.get("https://b2c.passport.rt.ru/")
    wait = WebDriverWait(browser, 15)

    #Нажимаем кнопку Cookies
    klic_input = wait.until(EC.visibility_of_element_located((By.ID, "cookies-tip-open")))
    klic_input.click()
    time.sleep(1)

    #Проверяем появления сообщения о Cookies
    try:
        cookie_banner = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(), 'Мы используем Cookie')]")
            )
        )
        print(" Всплывающее окно с Cookie найдено!")
    except TimeoutException:
        # если баннера нет тест провален
        browser.save_screenshot("no_cookie_banner.png")
        raise AssertionError(" Всплывающее окно с текстом 'Мы используем Cookie' не появилось.")
















