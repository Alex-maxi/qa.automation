import pytest
from src.application.utitapp.app import *


def test_user_age_is_43(user):
    assert user.age == 43


def test_sum():
    assert add_numbers(4, 5) == 9


def test_revarray():
    myarray = [9,8,7,6,5,4,3,2,1]
    assertarray = [1,2,3,4,5,6,7,8,9]
    assert revarray(myarray) == assertarray