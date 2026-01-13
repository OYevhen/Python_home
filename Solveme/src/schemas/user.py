from pydantic import BaseModel, field_validator
from ..enums.user_enums import Genders, Statuses, UserErrors


class User(BaseModel):
    id: int
    name: str
    email: str
    gender:Genders
    status: Statuses

    @field_validator('email')
    def check_that_dog_presented_in_email_address(cls, email):
        if '@' in email:
            return email
        else:
            raise ValueError(UserErrors.WRONG_EMAIL.value)





    #     "data": [
    #         {
    #             "id": 8115122,
    #             "name": "Bhishma Naik",
    #             "email": "naik_bhishma@ortiz-keebler.example",
    #             "gender": "female",
    #             "status": "active"
    #         },
    #         {
    #             "id": 8115121,
    #             "name": "Anala Acharya",
    #             "email": "anala_acharya@effertz.test",
    #             "gender": "female",
    #             "status": "inactive"
    #         },