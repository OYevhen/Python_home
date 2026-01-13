import pytest

from Solveme.src.baseclasses.response import Response
from Solveme.src.schemas.user import User

# resp = requests.get(SERVICE_URL)
# print(resp.json())
# print(resp.__getstate__())

def test_getting_users_list(get_users, make_number):
    Response(get_users).assert_status_code(200).validate(User)
    print(make_number)


@pytest.mark.development
@pytest.mark.production
@pytest.mark.skip('Issue #2322')
def test_another():
    assert 1 == 1

@pytest.mark.development
@pytest.mark.parametrize('first_val, sec_val, result', [
    (1, 2, 3),
    (-1, -2, -3),
    (-1, 2, 1),
    ('b', 1, None),
    ('b', 'a', None)
])
def test_calculator(first_val, sec_val, result, calculate):
    assert calculate(first_val, sec_val) == result

# {'meta': {'pagination': {'total': 1229, 'pages': 123, 'page': 1, 'limit': 10, 'links': {'previous': None, 'current': 'https://gorest.co.in/public/v1/users?page=1', 'next': 'https://gorest.co.in/public/v1/users?page=2'}}}, 'data': [{'id': 8115041, 'name': 'Esha Trivedi', 'email': 'trivedi_esha@ullrich-ferry.example', 'gender': 'female', 'status': 'active'}, {'id': 8115040, 'name': 'Mr. Ahilya Dutta', 'email': 'mr_ahilya_dutta@koss.test', 'gender': 'male', 'status': 'inactive'}, {'id': 8115037, 'name': 'Mr. Dhanadeepa Mahajan', 'email': 'dhanadeepa_mr_mahajan@wintheiser.test', 'gender': 'male', 'status': 'inactive'}, {'id': 8115031, 'name': 'Atreyi Chaturvedi V', 'email': 'chaturvedi_atreyi_v@walter.example', 'gender': 'female', 'status': 'inactive'}, {'id': 8115030, 'name': 'Dhana Chattopadhyay', 'email': 'chattopadhyay_dhana@keebler.example', 'gender': 'female', 'status': 'active'}, {'id': 8115029, 'name': 'Anish Varma', 'email': 'varma_anish@rodriguez.test', 'gender': 'female', 'status': 'active'}, {'id': 8115028, 'name': 'Rep. Prem Mishra', 'email': 'rep_mishra_prem@gottlieb.test', 'gender': 'female', 'status': 'active'}, {'id': 8115026, 'name': 'Rep. Vinay Tandon', 'email': 'vinay_rep_tandon@schimmel.test', 'gender': 'female', 'status': 'inactive'}, {'id': 8115025, 'name': 'Ekadant Reddy', 'email': 'reddy_ekadant@dare.test', 'gender': 'male', 'status': 'inactive'}, {'id': 8115024, 'name': 'Girika Kocchar DO', 'email': 'girika_kocchar_do@barton-blanda.example', 'gender': 'female', 'status': 'active'}]}