from enum import Enum

class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = 'Received status code is not equal to expected'
    WRONG_ELEMENT_COUNT = 'Received elements is not equal to expected'