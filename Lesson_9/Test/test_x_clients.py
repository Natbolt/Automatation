from Pages.Employee import Employer
from Pages.DataBase import DataBase


api = Employer("https://x-clients-be.onrender.com")
db = DataBase(
    "postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx")


# Получем список компаний
def test_get_list_of_employers():
    db.create_company('Nat company - Аня дебаг', 'best_company')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Nat", "Bolt", 8002000600)
    db_employer_list = db.get_list_employer(max_id)
    api_employer_list = api.get_list(max_id)
    assert len(db_employer_list) == len(api_employer_list)
    response = (api.get_list(max_id))[0]
    employer_id = response["id"]
    db.delete_employer(employer_id)
    db.delete(max_id)


# Добавление сотрудника в БД и сравнение с АПИ имяб статус и фамилию
def test_add_new_employer():
    db.create_company('Nat adding new employer', 'employer')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Nat", "Bolt", 8002000600)
    response = (api.get_list(max_id))[0]
    employer_id = response["id"]
    assert response["companyId"] == max_id
    assert response["firstName"] == "Nat"
    assert response["isActive"] == True
    assert response["lastName"] == "Bolt"
    db.delete_employer(employer_id)
    db.delete(max_id)


# Сравниваем информацию о сотруднике полученную 
# по API с информацией указанной при создании сотрудника
def test_assertion_data():
    db.create_company('Employer get id company', 'new')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Nat", "Bolt", 8002000600)
    employer_id = db.get_employer_id(max_id)
    get_api_info = (api.get_info(employer_id)).json()
    assert get_api_info["firstName"] == "Nat"
    assert get_api_info["lastName"] == "Bolt"
    assert get_api_info["phone"] == "8002000600"
    db.delete_employer(employer_id)
    db.delete(max_id)


# Сравниваем информацию о сотруднике полученную 
# по API с измененной информацией в БД о сотруднике
def test_update_user_info():
    db.create_company('New updating company', 'test')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Nat", "Bolt", 8002000600)
    employer_id = db.get_employer_id(max_id)
    db.update_employer_info("Bloom", employer_id)
    get_api_info = (api.get_info(employer_id)).json()
    assert get_api_info["firstName"] == "Bloom"
    assert get_api_info["lastName"] == "Bolt"
    assert get_api_info["isActive"] == True
    db.delete_employer(employer_id)
    db.delete(max_id)
