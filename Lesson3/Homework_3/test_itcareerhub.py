from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    # driver.set_window_size(1920, 1080)
    driver.get("https://itcareerhub.de/ru")
    yield driver
    driver.quit()


def test_logo_is_displayed(driver):
    logo = driver.find_element(By.CSS_SELECTOR, "img[alt='IT Career Hub']")

    assert logo.is_displayed()


def test_program_section(driver):
    program_links = driver.find_elements(By.CSS_SELECTOR, "a.tn-atom.t794__tm-link")

    assert any(p.is_displayed() for p in program_links)


def test_payment_section(driver):
    payment_links = driver.find_elements(By.CSS_SELECTOR, "a[href='#rec1921734713']")

    assert any(p.is_displayed() for p in payment_links)


def test_about_us_section(driver):
    about_us_links = driver.find_elements(By.CSS_SELECTOR, "a[href='/ru/o-nas']")

    assert any(a.is_displayed() for a in about_us_links)


def test_reviews_section(driver):
    review_links = driver.find_elements(By.CSS_SELECTOR, ".t396__elem a[href='/reviews']")

    assert any(r.is_displayed() for r in review_links)


def test_language_section(driver):
    ru = driver.find_elements(By.CSS_SELECTOR, "a[href='/ru']")
    de = driver.find_elements(By.CSS_SELECTOR, "a[href='/']")

    assert any(r.is_displayed() and r.text.strip().lower() == "ru" for r in ru)
    assert any(d.is_displayed() and d.text.strip().lower() == "de" for d in de)


def test_phone_button(driver):
    driver.get("https://itcareerhub.de/reviews")

    sleep(5)

    phone_icons = driver.find_elements(By.CSS_SELECTOR, "a[href='#popup:form-tr3'] img")
    for icon in phone_icons:
        if icon.is_displayed():
            icon.click()
            break

    sleep(5)

    texts = driver.find_elements(By.CSS_SELECTOR, "div.tn-atom[field='tn_text_1711363912027']")

    assert any(
        t.is_displayed() and
        "Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вами" in t.text
        for t in texts
    )
