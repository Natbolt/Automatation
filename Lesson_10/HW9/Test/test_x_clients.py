import pytest
import allure
from Pages.Employee import Employer
from Pages.DataBase import DataBase


api = Employer("https://x-clients-be.onrender.com")
db = DataBase("postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx")

@allure.epic("X-clients")
@allure.severity(severity_level='normal')
@allure.title("Список сотрудников")
@allure.description("Получаем список сотрудников из БД и АПИ, после чего сравниваем их")
@allure.feature('Тест 1')
def test_get_list_of_employers():
    with allure.step("БД - Создаем компанию"):
        db.create_company('Nat company', 'best_company')
    with allure.step("БД - Получаем ID последней созданной компании"):
        max_id = db.last_company_id()
    with allure.step("БД - Добавляем сотрудника в компанию"):
        db.create_employer(max_id, "Nat", "Bolt", 8002000600)
    with allure.step("БД - Получем список сотрудников из последней созданной компании"):
        db_employer_list = db.get_list_employer(max_id)
    with allure.step("API - Получем список сотрудников из последней созданной компании"):
        api_employer_list = api.get_list(max_id)
    with allure.step("Сравниваем списки сотрудников полученных из БЗ и через API"):
        assert len(db_employer_list) == len(api_employer_list)
    with allure.step("БД - Удаляем созданного сотрудника"):
        response = (api.get_list(max_id))[0]
        employer_id = response["id"]
        db.delete_employer(employer_id)
    with allure.step("БД - Удаляем последнюю созданную компанию"):
        db.delete(max_id)

@allure.epic("X-clients")
@allure.severity(severity_level='critical')
@allure.title("Добавление сотрудников")
@allure.description("Добавление сотрудника в БД и сравниваем с АПИ имя, статус и фамилию")
@allure.feature('Тест 2')
def test_add_new_employer():
    with allure.step("БД - Создаем компанию"):
        db.create_company('Nat adding new employer', 'employer')
    with allure.step("БД - Получаем ID последней созданной компании"):
        max_id = db.last_company_id()
    with allure.step("БД - Добавляем сотрудника в компанию"):
        db.create_employer(max_id, "Nat", "Bolt", 8002000600)
    with allure.step("Сравниваем данные о сотруднике в БД с АПИ имя, статус и фамилию"):
        response = (api.get_list(max_id))[0]
        employer_id = response["id"]
        assert response["companyId"] == max_id
        assert response["firstName"] == "Nat"
        assert response["isActive"] == True
        assert response["lastName"] == "Bolt"
    with allure.step("БД - Удаляем созданного сотрудника"):
        db.delete_employer(employer_id)
    with allure.step("БД - Удаляем последнюю созданную компанию"):
        db.delete(max_id)

@allure.epic("X-clients")
@allure.severity(severity_level='critical')
@allure.title("Сравнение информации о сотруднике")
@allure.description("Сравниваем информацию о сотруднике полученную по API с информацией указанной при создании сотрудника")
@allure.feature('Тест 3')
def test_assertion_data():
    with allure.step("БД - Создаем компанию"):
        db.create_company('Employer get id company', 'new')
    with allure.step("БД - Получаем ID последней созданной компании"):
        max_id = db.last_company_id()
    with allure.step("БД - Добавляем сотрудника в компанию"):
        db.create_employer(max_id, "Nat", "Bolt", 8002000600)
        employer_id = db.get_employer_id(max_id)
    with allure.step("Сравниваем информацию о сотруднике полученную по API с информацией указанной при создании сотрудника"):
        get_api_info = (api.get_info(employer_id)).json()
        assert get_api_info["firstName"] == "Nat"
        assert get_api_info["lastName"] == "Bolt"            
        assert get_api_info["phone"] == "8002000600"
    with allure.step("БД - Удаляем созданного сотрудника"):
        db.delete_employer(employer_id)
    with allure.step("БД - Удаляем последнюю созданную компанию"):
        db.delete(max_id)

@allure.epic("X-clients")
@allure.severity(severity_level='critical')
@allure.title("Изменение информации о сотруднике")
@allure.description("Сравниваем информацию о сотруднике полученную по API с измененной информацией в БД о сотруднике")
@allure.feature('Тест 4')
def test_update_user_info():
    with allure.step("БД - Создаем компанию"):
        db.create_company('New updating company', 'test')
    with allure.step("БД - Получаем ID последней созданной компании"):
        max_id = db.last_company_id()
    with allure.step("БД - Добавляем сотрудника в компанию"):
        db.create_employer(max_id, "Nat", "Bolt", 8002000600)
        employer_id = db.get_employer_id(max_id)
    with allure.step("БД - Изменяем информацию о сотруднике"):
        db.update_employer_info("Bloom", employer_id)
    with allure.step("Сравниваем информацию о сотруднике полученную по API с измененной информацией в БД о сотруднике"):
        get_api_info = (api.get_info(employer_id)).json()
        assert get_api_info["firstName"] == "Bloom"
        assert get_api_info["lastName"] == "Bolt"
        assert get_api_info["isActive"] == True
    with allure.step("БД - Удаляем созданного сотрудника"):
        db.delete_employer(employer_id)
    with allure.step("БД - Удаляем последнюю созданную компанию"):
        db.delete(max_id)