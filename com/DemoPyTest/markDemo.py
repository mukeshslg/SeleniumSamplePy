import pytest


@pytest.fixture(autouse=True)
def test_startup():
    print("Starting machine")


@pytest.mark.windows
def test_windows_xp(test_startup):
    print("This is windows xp:")


@pytest.mark.windows
def test_windows_7(test_startup):
    print("this is windows7:")


@pytest.mark.mac
def test_mac_pro(test_startup):
    print("this is mac book pro:")
