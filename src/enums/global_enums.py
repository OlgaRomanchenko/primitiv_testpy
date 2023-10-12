from enum import Enum

class GlobalErrorMassages(Enum):
    WRONG_STATUS_CODE = "received status code is not equal to expected"