import os
from dotenv import load_dotenv
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv()
# Получение данных из .env
TEST_PHONE = os.getenv("TEST_PHONE")
TEST_PASSWORD = os.getenv("TEST_PASSWORD")
TEST_EMAIL = os.getenv("TEST_EMAIL")
TEST_FAMILY = os.getenv("TEST_FAMILY")
TEST_LOGIN = os.getenv("TEST_LOGIN")
TEST_CHET = os.getenv("TEST_CHET")
TEST_KOD = os.getenv("TEST_KOD")
TEST_NAME = os.getenv("TEST_NAME")
TEST_REGION = os.getenv("TEST_REGION")

#Создаем словарь с данными для тестов
ALL_CREDENTIALS = {
    "phone": TEST_PHONE,
    "password": TEST_PASSWORD,
    "name": TEST_NAME,
    "email": TEST_EMAIL,
    "family": TEST_FAMILY,
    "login": TEST_LOGIN,
    "chet": TEST_CHET,
    "region": TEST_REGION,
    "kod": TEST_KOD,
}


@pytest.fixture(scope="module")
def browser():
    """Инициализирует и закрывает браузер."""
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture
def credentials():
    """Возвращает словарь со всеми учетными данными."""
    return ALL_CREDENTIALS



@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """автоскриншот при падении теста."""
    outcome = yield
    rep = outcome.get_result()
    # Делаем скриншот только если тест упал на этапе выполнения (call)
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("browser")
        if driver:
            test_name = item.name.replace("/", "_").replace(":", "_").replace(" ", "_")
            # Создаем папку screenshots, если её нет
            os.makedirs("screenshots", exist_ok=True)
            screenshot_path = f"screenshots/fail_{test_name}.png"

            try:
                driver.save_screenshot(screenshot_path)
                # Добавляем путь к скриншоту в сообщение об ошибке
                rep.longrepr = f"{rep.longrepr}\n\n Автоскриншот сохранен: {os.path.abspath(screenshot_path)}"
            except Exception as e:
                print(f"Не удалось сохранить скриншот: {e}")