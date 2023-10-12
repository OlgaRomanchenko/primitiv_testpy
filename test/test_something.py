import requests
from config import SERVICE_URL
from src.enums.global_enums import GlobalErrorMassages
def test_getting_post():
    response = requests.get(url=SERVICE_URL)
    assert response.status_code == 200, GlobalErrorMassages.WRONG_STATUS_CODE.value
    print(response)
