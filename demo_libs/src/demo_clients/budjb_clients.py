import requests
from .constants import STATIC_BUDJB_BASE_URL


class TestClient(object):
    def __init__(self, base_url=STATIC_BUDJB_BASE_URL):
        self.base_url = base_url

    def get_test(self, name):
        r = requests.get(url=f"{self.base_url}/test.php?name={name}")
        r.raise_for_status
        return r.json
