import pytest
from string_utils import StringUtils

utils = StringUtils()

"""capitalize"""


def test_capitalize():
    """POSITIVE"""
    assert utils.capitalize("skypro") == "Skypro"
    assert utils.capitalize("hello world") == "Hello world"
    assert utils.capitalize("123") == "123"
    assert utils.capitalize("привет") == "Привет"
    assert utils.capitalize("$kypro") == "$kypro"
    """NEGATIVE"""
    assert utils.capitalize("") == ""
    assert utils.capitalize(" ") == " "
    assert utils.capitalize("hello w0rld") == "Hello w0rld"
    assert utils.capitalize("---") == "---"
    assert utils.capitalize("skypro   ") == "Skypro   "


"""trim"""


def test_trim():
    """POSITIVE"""
    assert utils.trim("   skypro") == "skypro"
    assert utils.trim("   hello world   ") == "hello world   "
    assert utils.trim("   SKY   ") == "SKY   "
    assert utils.trim("   123") == "123"
    assert utils.trim("   привет ") == "привет "
    """NEGATIVE"""
    assert utils.trim("") == ""
    assert utils.trim(" ") == ""
    assert utils.trim(" --- ") == "--- "


"""to_list"""


@pytest.mark.parametrize('string, delimeter, result', [
    # POSITIVE
    ("cat,dog,bird", ",", ["cat", "dog", "bird"]),
    ("1/2/3/4/5", "/", ["1", "2", "3", "4", "5"]),
    ("Aries★Taurus★Gemini★Cancer★Leo", "★", ["Aries", "Taurus", "Gemini", "Cancer", "Leo"]),
    # NEGATIVE
    ("", None, []),
    ("1,2,3,4 5", None, ["1", "2", "3", "4 5"]),
])
def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = utils.to_list(string)
    else:
        res = utils.to_list(string, delimeter)
    assert res == result


"""contains"""

@pytest.mark.parametrize('string, symbol, result', [

    ("cat", "c", True),
    ("dog", "g", True),
    ("кресло-качалка", "-", True),
    ("8921", "2", True),
    ("", "", True),
    ("cat", "с", False), # с-кириллицей
    ("Skypro", "s", False),
    ("", "-", False),
])
def test_contains(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result



"""delete_symbol"""

@pytest.mark.parametrize('string, symbol, result', [
    ("Привет", "П", "ривет"),
    ("Skyeng", "e", "Skyng"),
    ("cat", "c", "at"),
    ("123", "3", "12"),
    ("чайная ложка", " ", "чайнаяложка"),

    ("dog", "a", "dog"),
    ("", "", ""),
    ("", "i", ""),
    ("cat", "с", "cat"), # с-кириллицей
    ("summer", "", "summer"),
    ("осень", " ", "осень"), 
])
def test_delete_symbol(string, symbol, result):
    res = utils.delete_symbol(string, symbol)
    assert res == result


"""starts_with"""


@pytest.mark.parametrize('string, symbol,, result', [

    ("аналитик", "а", True),
    ("", "", True),
    ("Разработчик", "Р", True),
    ("Java-разработчик", "J", True),
    ("Интернет-маркетолог", "И", True),
    ("123", "1", True),

    ("Графический дизайнер", "г", False),
    ("тестировщик", "Т", False),
    ("", "%", False),
    ("python", "r", False),
    ("123", "3", False),
])
def test_starts_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result


"""end_with"""


@pytest.mark.parametrize('string, symbol,, result', [

    ("аналитик", "к", True),
    ("", "", True),
    ("Разработчик", "к", True),
    ("Java-разработчик", "к", True),
    ("Интернет-маркетолог", "г", True),
    ("123", "3", True),

    ("Графический дизайнер", "г", False),
    ("тестировщик", "k", False), # k- латиница
    ("", "%", False),
    ("python", "r", False),
    ("123", "2", False),
])
def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result


"""is_empty"""

@pytest.mark.parametrize('string, result', [
    ("", True),
    (" ", True),
    ("   ", True),

    ("isn't empty", False),
    ("python", False),
    ("678", False),
])
def test_is_EMPTY(string, result):
    res = utils.is_empty(string)
    assert res == result


"""list_to_string"""


@pytest.mark.parametrize('lst, joiner, result', [

    (["V", "I", "P"], ".", "V.I.P"),
    (["Python", "Разработчик"], "-", "Python-Разработчик"),
    (["А", "Б"], "и", "АиБ"),
    (["p", "y", "t", "h", "o", "n"], "", "python"),

    ([], None, ""),
    ([], ",", ""),
    ([], "pytest", "")
])
def test_list_to_string(lst, joiner, result):
    if joiner == None:
        res = utils.list_to_string(lst)
    else:
        res = utils.list_to_string(lst, joiner)
    assert res == result