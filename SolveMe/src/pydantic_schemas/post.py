from pydantic import BaseModel, validator, Field

class Post(BaseModel):
    # id: int
    id: int = Field(le=3)
    title: str
    # name: str = Field(alias='_name')

    # @validator('id')
    # def check_that_is_less_than_two(cls, v):
    #     if v > 2:
    #         raise ValueError('ID is not less than two')
    #     else:
    #         return v


# [{'id': 1, 'title': 'Post 1', 'name': 'Igor'}]
