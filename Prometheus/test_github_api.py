import pytest
from gihub import GitHub
@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('OYevhen')
    assert user['login'] == 'OYevhen'

@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('orelyevhen')
    assert r['message'] == 'Not Found'