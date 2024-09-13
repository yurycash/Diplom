import requests
import allure


chitaigorod = "https://web-gate.chitai-gorod.ru/api/v1/"
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIwOTk1MTY2LCJpYXQiOjE3MjYyMjMyODcsImV4cCI6MTcyNjIyNjg4NywidHlwZSI6MjB9.NF3NTYZrKw0xTf7AKnoeHPTmss6Bal2k8UKAYasVwvI"
headers = {"authorization": f"Bearer {token}"}


@allure.feature("API")
@allure.title("Добавление товара в корзину.")
@allure.description("Добавление товара в корзину через API.")
def test_add_cart_product():
    body = {"id": 3038460, "adData": {
        "item_list_name": "profile-bookmarks", "product_shelf": ""}}
    with allure.step("Добавление товара в корзину."):
        response = requests.post(
            chitaigorod + "cart/product", headers=headers, json=body)
    with allure.step("Проверка статус кода"):
        assert response.status_code == 200


@allure.feature("API")
@allure.title("Изменение кол-ва товара в корзине.")
@allure.description("Изменение кол-ва товара в корзине через API.")
def test_changing_quantity_in_cart():
    body = [{"id": 125362739, "quantity": 10}]
    with allure.step("Изменение количества товара."):
        response = requests.put(chitaigorod + "cart",
                                headers=headers, json=body)
    with allure.step("Проверка статус кода"):
        assert response.status_code == 200


@allure.feature("API")
@allure.title("Добавление товара в избранное.")
@allure.description("Добавление товара в избранное через API.")
def test_add_product_in_bookmarks():
    with allure.step("Добавление товара в избранное."):
        body = {"id": 3038460}
        response = requests.post(chitaigorod + "bookmarks",
                                 headers=headers, json=body)
    with allure.step("Проверка статус кода"):
        assert response.status_code == 201


@allure.feature("API")
@allure.title("Удаление товара из избранного.")
@allure.description("Удаление товара из избранного через API.")
def test_delete_product_in_bookmarks():
    with allure.step("Удаление товара из избранного."):
        body = {"id": 3038460}
        response = requests.delete(chitaigorod + "bookmarks",
                                   headers=headers, json=body)
    with allure.step("Проверка статус кода"):
        assert response.status_code == 204


@allure.feature("API")
@allure.title("Изменение персональных данных.")
@allure.description("Изменение персональных данных через API.")
def test_editing_personal_data():
    with allure.step("Изменение персональных данных."):
        body = {"lastName": "Иванов",
                "firstName": "Иван",
                "middleName": "Иванович",
                "birthday": "1980-01-01",
                "phone": "79999999999",
                "email": "yury.cash@yandex.ru",
                "phoneCountry": ""}
        response = requests.patch(
            chitaigorod + "profile/personal-data", headers=headers, json=body)
    with allure.step("Проверка статус кода"):
        assert response.status_code == 200
