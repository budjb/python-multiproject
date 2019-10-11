from demo_clients import constants
import requests_mock
import main


def test_main_go():
    with requests_mock.Mocker() as m:
        m.get(
            f"{constants.STATIC_BUDJB_BASE_URL}/test.php?name=foo", json={"foo": "bar"}
        )

        main.go("foo")
