from enum import Enum

class GlobalErrors(Enum):
    WRONG_STATUS_CODE = 'Received status code is not equal to expected'
    WRONG_ELEMENT_COUNT = 'Received elements is not equal to expected'