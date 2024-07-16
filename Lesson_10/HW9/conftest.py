import pytest
import requests
from constants import url

@pytest.fixture()
def get_token(username='stella', password='sun-fairy'):
    log_pass = {'username': username, 'password' : password}
    resp_token = requests.post(url + '/auth/login', json=log_pass)
    token = resp_token.json()['userToken']
    return token
