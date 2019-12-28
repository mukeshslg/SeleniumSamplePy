import pytest


@pytest.fixture
def supply_x_y_z():
    print("Fixture running..")
    x = 1
    y = 2
    z = 3
    return [x, y, z]


def test_accept_x(supply_x_y_z):
    x = 1
    assert supply_x_y_z[0] == x, "value of x not matching"


def test_accept_y(supply_x_y_z):
    y = 22
    assert supply_x_y_z[1] == y, "value of y not matching"





# if __name__ == '__main__':
#     test_accept_x(supply_x_y_z())
#     test_accept_y(supply_x_y_z())
