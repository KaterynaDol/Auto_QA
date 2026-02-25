from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://itcareerhub.de/ru")
    yield driver
    driver.quit()


def test_logo_is_displayed(driver):
    logo = driver.find_element(By.CSS_SELECTOR, "img[alt='IT Career Hub']")

    assert logo.is_displayed()


def test_program_section(driver):
    program = driver.find_element(By.LINK_TEXT, "Программы")

    assert program.is_displayed()


def test_payment_section(driver):
    payment = driver.find_element(By.LINK_TEXT, "Способы оплаты")

    assert payment.is_displayed()


def test_about_us_section(driver):
    about_us = driver.find_element(By.LINK_TEXT, "О нас")

    assert about_us.is_displayed()


def test_reviews_section(driver):
    reviews = driver.find_element(By.LINK_TEXT, "Отзывы")

    assert reviews.is_displayed()


def test_language_section(driver):
    ru = driver.find_element(By.LINK_TEXT, "ru")
    de = driver.find_element(By.LINK_TEXT, "de")

    assert ru.is_displayed()
    assert de.is_displayed()

    de.click()
    sleep(3)
    assert "/ru" not in driver.current_url

    ru = driver.find_element(By.LINK_TEXT, "ru")
    ru.click()
    sleep(3)
    assert "/ru" in driver.current_url


def test_phone_button(driver):
    driver.get("https://itcareerhub.de/reviews")

    sleep(3)

    phone_icon = driver.find_element(By.CSS_SELECTOR, "a[href='#popup:form-tr3'] img")

    assert phone_icon.is_displayed()
    phone_icon.click()

    sleep(5)

    popup_text = driver.find_element(By.CSS_SELECTOR, ".t396__elem.tn-elem.tn-elem__13803069911711363912027")

    assert popup_text.is_displayed()
    assert "Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вами" in popup_text.text
