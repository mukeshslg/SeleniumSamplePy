import pytest


@pytest.fixture  # <-this is decorator in python
def supply_x_y_z():
    print("Fixture running..")
    x = 1
    y = 2
    z = 3
    return [x, y, z]


@pytest.mark.skip(reason="don't want to run test_accept_x now")
def test_accept_x(supply_x_y_z):
    x = 1
    assert supply_x_y_z[0] == x, "value of x not matching"


@pytest.mark.skipif((3 > 5), reason="trying to skip test_accept_y")
def test_accept_y(supply_x_y_z):
    y = 2
    assert supply_x_y_z[1] == y, "value of y not matching"


# if __name__ == '__main__':
#     test_accept_x(supply_x_y_z())
#     test_accept_y(supply_x_y_z())
