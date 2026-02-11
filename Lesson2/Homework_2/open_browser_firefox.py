import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By

from webdriver_manager.firefox import GeckoDriverManager

from time import sleep


# Настройка драйвера для Firefox с использованием WebDriverManager
# driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

@pytest.fixture
def driver():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_payment_section(driver):
    driver.get('https://itcareerhub.de/ru')
    sleep(3)

    driver.find_element(By.LINK_TEXT, "Способы оплаты").click()
    sleep(3)

    driver.save_screenshot('payment_screenshot.png')
