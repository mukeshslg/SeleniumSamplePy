import pytest


@pytest.mark.parametrize("x,y", [(2, 4)])
def test_startup(x,y):
    print("value:", x, y)


@pytest.mark.windows
def test_windows_xp(test_startup):
    print("This is windows xp:")


@pytest.mark.windows
def test_windows_7(test_startup):
    print("this is windows7:")


@pytest.mark.mac
def test_mac_pro(test_startup):
    print("this is mac book pro:")
