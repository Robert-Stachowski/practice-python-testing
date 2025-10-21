import pytest
from user import validate_user

@pytest.fixture
def user_data():
    return {
        "email":"jannowak@przyklad.pl",
        "name": "Janek",
        "age": 55
    }

@pytest.fixture
def failed_data():
    return []




def test_valid_user_data(user_data):
    assert validate_user(user_data) is True

def test_failed_when_data_not_dict(failed_data):
    assert validate_user(failed_data) is False

def test_failed_data_is_none():
    assert validate_user(None) is False


# Age
def test_valid_age_min(user_data):
    user_data["age"] = 18
    assert validate_user(user_data) is True

def test_failed_age_under_min(user_data):
    user_data["age"] = 17
    assert validate_user(user_data) is False

def test_failed_age_string(user_data):
    user_data["age"] = "55"
    assert validate_user(user_data) is False   

def test_failed_no_age(user_data):
    user_data["age"] = None
    assert validate_user(user_data) is False

def test_failed_del_age(user_data):
    del user_data["age"]
    assert validate_user(user_data) is False

def test_failed_true_age(user_data):
    user_data["age"] = True
    assert validate_user(user_data) is False


# Name
def test_failed_name_user_data(user_data):
    user_data["name"] = "M9chał"
    assert validate_user(user_data) is False

def test_failed_name_user_data_digits(user_data):
    user_data["name"] = "123456"
    assert validate_user(user_data) is False

def test_failed_name_user_data_space(user_data):
    user_data["name"] = " Michał "
    assert validate_user(user_data) is False

def test_failed_empty_string(user_data):
    user_data["name"] = ""
    assert validate_user(user_data) is False  

def test_failed_no_name(user_data):
    user_data["name"] = None
    assert validate_user(user_data) is False

def test_valid_name_with_polish_chars(user_data):
    user_data["name"] = "Łukasz"
    assert validate_user(user_data) is True

def test_failed_del_name(user_data):
    del user_data["name"]
    assert validate_user(user_data) is False


# email
def test_failed_email_user_data_no_at_symbol(user_data):
    user_data["email"] = "jannnowak.przyklad.pl"
    assert validate_user(user_data) is False

def test_failed_email_user_data_tld(user_data):
    user_data["email"] = "jannnowak@przyklad.xo"
    assert validate_user(user_data) is False

def test_failed_no_email(user_data):
    user_data["email"] = None
    assert validate_user(user_data) is False

def test_failed_email_user_data_space(user_data):
    user_data["email"] = " jannnowak@przyklad.pl "
    assert validate_user(user_data) is False

def test_failed_del_email(user_data):
    del user_data["email"]
    assert validate_user(user_data) is False