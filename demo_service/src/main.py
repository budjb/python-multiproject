from demo_clients import budjb_clients


def go(name):
    return budjb_clients.TestClient().get_test(name)
