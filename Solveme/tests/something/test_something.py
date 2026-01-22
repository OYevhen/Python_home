import requests
import pytest


@pytest.mark.parametrize('status', [
    'ACTIVE',
    'BANNED',
    'DELETED',
    'INACTIVE'
])
def test_something(status, get_player_generator):
    print(get_player_generator.build())


@pytest.mark.parametrize('balance_value', [
    '100',
    '0',
    '-10',
    'vbvbv'
])
def test_something(balance_value, get_player_generator):
    print(get_player_generator.set_balance(balance_value).build())