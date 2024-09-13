import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import allure


@pytest.fixture()
def chrome_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@allure.feature("UI")
@allure.title("Поиск книги 'Через пески'.")
@allure.description("Проверка работы поисковой строки.")
def test_search(chrome_browser):
    with allure.step("Перейти на главную страницу Читай-Город"):
        chrome_browser.get("https://www.chitai-gorod.ru/")
    with allure.step("Ввести в строке поиска 'Через пески'."):
        chrome_browser.find_element(
            By.CSS_SELECTOR, ".header-search__input").send_keys("Через пески")
    with allure.step("Кликнуть на лупу в строке поиска"):
        chrome_browser.find_element(
            By.CSS_SELECTOR, ".header-search__button-icon").click()
        sleep(2)  # локатор не успевает прогружаться, браузер закрывается
    with allure.step("Проверка наличия искомой книги"):
        assert chrome_browser.find_element(
            By.CSS_SELECTOR, ".product-title__head").text == "Через пески"


@allure.feature("UI")
@allure.title("Корзина.")
@allure.description("Проверка отсуствия товаров в корзине.")
def test_cart(chrome_browser):
    with allure.step("Перейти на главную страницу Читай-Город"):
        chrome_browser.get("https://www.chitai-gorod.ru/")
    with allure.step("Кликнуть по ярлыку корзины"):
        chrome_browser.find_element(
            By.CSS_SELECTOR, ".header-cart__icon.header-cart__icon--desktop").click()
    with allure.step("Проверка наличия текста 'В корзине ничего нет'"):
        assert chrome_browser.find_element(
            By.CSS_SELECTOR, ".empty-title").text == "В корзине ничего нет"


@allure.feature("UI")
@allure.title("Строка поиска.")
@allure.description("Проверка принятия сторокой поиска невалидного значения.")
def test_search_invalid(chrome_browser):
    with allure.step("Перейти на главную страницу Читай-Город"):
        chrome_browser.get("https://www.chitai-gorod.ru/")
    with allure.step("Ввести в строке поиска $#%^&"):
        chrome_browser.find_element(
            By.CSS_SELECTOR, ".header-search__input").send_keys("$#%^&")
    with allure.step("Кликнуть на лупу в строке поиска"):
        chrome_browser.find_element(
            By.CSS_SELECTOR, ".header-search__button-icon").click()
    with allure.step("Проверка наличия текста 'Похоже, у нас такого нет'."):
        assert chrome_browser.find_element(
            By.CSS_SELECTOR, ".catalog-empty-result__header").text == "Похоже, у нас такого нет"


@allure.feature("UI")
@allure.title("Переход по ссылке 'НОВИНКИ ЛИТЕРАТУРЫ'.")
@allure.description("Проверка перехода на страницу 'НОВИНКИ ЛИТЕРАТУРЫ'.")
def test_new(chrome_browser):
    with allure.step("Перейти на главную страницу Читай-Город"):
        chrome_browser.get("https://www.chitai-gorod.ru/")
    with allure.step("Кликнуть по заголовку 'НОВИНКИ ЛИТЕРАТУРЫ'."):
        result = chrome_browser.find_elements(
            By.CSS_SELECTOR, ".app-title--link")
    with allure.step("Проверка перехода на страницу 'НОВИНКИ ЛИТЕРАТУРЫ'."):
        assert result[0].text == "НОВИНКИ ЛИТЕРАТУРЫ"


@allure.feature("UI")
@allure.title("Заголовки на главной странице.")
@allure.description("Проверка количества заголовков на главной странице.")
def test_number_of_titles(chrome_browser):
    with allure.step("Перейти на главную страницу Читай-Город"):
        chrome_browser.get("https://www.chitai-gorod.ru/")
    result = chrome_browser.find_elements(By.CSS_SELECTOR, ".app-title--link")
    with allure.step("Проверка количества заголовков"):
        assert len(result) == 4
