import requests

from SolveMe.configuration import SERVICE_URL

from SolveMe.src.baseclasses.response import Response
from SolveMe.src.schemas.post import POST_SCHEMA
from SolveMe.src.pydantic_schemas.post import Post


# def test_equal():
#     assert 1 == 2, "Number is not equal to expected"

def test_getting_posts():
    r = requests.get(url=SERVICE_URL)
    response = Response(r)
    # response.assert_status_code(200).validate(POST_SCHEMA)
    response.assert_status_code(200).validate2(Post)

# [{'id': 1, 'title': 'Post 1'}, {'id': 2, 'title': 'Post 2'}, {'id': 3, 'title': 'Post 3'}]
