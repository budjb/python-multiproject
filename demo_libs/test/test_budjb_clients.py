from demo_clients import constants, budjb_clients
import requests_mock


def test_budjb_get_test():
    client = budjb_clients.TestClient()

    with requests_mock.Mocker() as m:
        m.get(
            f"{constants.STATIC_BUDJB_BASE_URL}/test.php?name=foo", json={"foo": "bar"}
        )

        client.get_test("foo") == {"foo": "bar"}
