from  ..enums.global_enums import GlobalErrors

class Response:

    def __init__(self, response):
        self.response = response
        self.response_json = response.json().get('data')
        self.response_status = response.status_code

    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.model_validate(item)
        else:
            schema.model_validate(self.response_json)


    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, self
        else:
            assert self.response_status == status_code, self
        return self

    def __str__(self):
        return f'\n Status code: {self.response_status}, \n Requested url: {self.response.url}, \n Response body: {self.response_json}'