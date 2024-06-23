import pytest
import requests
from Lesson_8.Pages.Employee import Employer, Company

employer = Employer()
company = Company()

# Авторизация
def test_authorization(get_token):
    token = get_token
    assert token is not None
    assert isinstance(token, str)

# Получение ID последней компании
def test_getcompany_id():
    company_id = company.last_active_company_id()
    """Проверяем, что токен не пустой"""
    assert company_id is not None
    """Проверяем, что токен имеет строковый формат"""
    assert str(company_id).isdigit()

# Добавление сотрудника
def test_add_empoyer(get_token):
    token = str(get_token)
    com_id = company.last_active_company_id()
    body_employer = {
       'id': 0,
       'firstName': 'Harry',
       'lastName': 'Potter',
       'middleName': 'James',
       'companyId': com_id,
       'email': 'test@mail.ru',
       'url': 'string',
       'phone': 'string',
       'birthdate': '1980-07-20T11:19:32.967Z',
       'isActive': 'true'
    }
    new_employer_id = (employer.add_new(token, body_employer))['id']
    assert new_employer_id is not None
    assert str(new_employer_id).isdigit()

    info = employer.get_info(new_employer_id)
    assert info.json()['id'] == new_employer_id
    assert info.status_code == 200

# Проверяем обязательность полей для запроса на создание клиента

"""Проверяем невозможность создания клиента без токена"""


def test_add_empoyer_without_token():
    com_id = company.last_active_company_id()
    token = ""
    body_employer = {
       'id': 0,
       'firstName': 'Harry',
       'lastName': 'Potter',
       'middleName': 'James',
       'companyId': com_id,
       'email': 'test@mail.ru',
       'url': 'string',
       'phone': 'string',
       'birthdate': '1980-07-20T11:19:32.967Z',
       'isActive': 'true'
    }
    new_employer = employer.add_new(token, body_employer)
    assert new_employer['message'] =='Unauthorized'


"""Проверяем невозможность создания клиента без тела запроса"""


def test_add_empoyer_without_body(get_token):
    token = str(get_token)
    com_id = company.last_active_company_id()
    body_employer = {}
    new_employer = (employer.add_new(token, body_employer))
    assert new_employer['message'] =='Internal server error'

# Получение списка сотрудников
def test_get_employer():
    com_id = company.last_active_company_id()
    list_employers = employer.get_list(com_id)
    assert isinstance(list_employers, list)

# Проверяем обязательность полей для запроса на получение списка сотрудников компании


"""Проверяем невозможность получения списка сотрудников компании без ID компании"""


def test_get_list_employers_missing_company_id():
    try:
        employer.get_list()
    except TypeError  as e:
        assert str(
            e) == "Employer.get_list() missing 1 required positional argument: 'company_id'"


"""Проверяем невозможность получения списка сотрудников компании,
заполняя обязательнон поле 'ID компании' невалидным значением
(пустая строка)"""


def test_get_list_employers_invalid_company_id():
    try:
        employer.get_list('')
    except TypeError as e:
        assert str(
            e) == "Employer.get_list() missing 1 required positional argument: 'company_id'"


"""Проверяем невозможность получения информации о сотруднике без ID сотрудника"""


def test_get_info_new_employers_missing_employer_id():
    try:
        employer.get_info()
    except TypeError as e:
        assert str(
        e) == "Employer.get_info() missing 1 required positional argument: 'employee_id'"

# Изменение информации о сотруднике
def test_change_employer_info(get_token):
    token = str(get_token)
    com_id = company.last_active_company_id()
    body_employer = {
        'id': 0,
        'firstName': 'Harry',
        'lastName': 'Potter',
        'middleName': 'James',
        'companyId': com_id,
        'email': 'test@mail.ru',
        'url': 'string',
        'phone': 'string',
        'birthdate': '1980-07-20T11:19:32.967Z',
        'isActive': 'true'
    }
    just_employer = employer.add_new(token, body_employer)
    id = just_employer['id']
    body_change_employer = {
        'lastName': 'Black',
        'email': '2test@mail.ru',
        'url': 'string',
        'phone': 'string',
        'isActive': 'true'
    }
    employer_changed = employer.change_info(token, id, body_change_employer)
    assert employer_changed.status_code == 200

    assert id == employer_changed.json()['id']
    assert (employer_changed.json()["email"]
            ) == body_change_employer.get("email")


# Проверяем обязательность полей в запросе на изменение информации о сотруднике


"""Проверяем невозможность изменения информации о сотруднике без полей 'ID сотрудника', 'token', 'body'"""


def test_employers_missing_id_and_token():
    try:
        employer.change_info()
    except TypeError as e:
        assert str(
            e) == "Employer.change_info() missing 3 required positional arguments: 'token', 'employee_id', and 'body'"