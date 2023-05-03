"""The `pytest` module provides a testing framework for Python"""
import pytest
from src.application.utitapp.app import Apps
from src.application.api.github_api_client import GitHubApiClient
from src.libraries.helpers import read_data_from_csv
from src.config.config import CONFIG
from src.data.models.users import User


input_data = CONFIG.get("TEST_DATA")
sum_test_data = read_data_from_csv(input_data)
apps = Apps()
api = GitHubApiClient()


@pytest.mark.math
@pytest.mark.parametrize("data, result", sum_test_data)
def test_get_sum_of_digits(data: str, result: int):
    """
    Test Sum function which sum all input digits. Example 12345=15. 
    Args:
        data (str): data from CSV file. Generator. 
        result (int): Expected data
    """
    assert apps.get_sum_of_digits(data) == int(result)


@pytest.mark.set_get
def test_user_age_and_name_dict():
    """
    Test, checking User Class builder.
    """
    user = User().set_name('Tyson').set_age(36).set_lastname('Fury').set_email(
        'tyson@gmail.com').set_gender('Male').build_user_obj()
    assert user['age'] == 36 and user['name'] == "Tyson" and user['email'] == 'tyson@gmail.com'


@pytest.mark.set_get
def test_user_age_and_name_class():
    """
    Test, checking User Class setting data like Class parameters.
    """
    user = User(36, 'Tyson', 'Fury', 'tyson@gmail.com', 'Male')
    assert user.get_age() == 36 and user.get_name(
    ) == "Tyson" and user.get_gender() == 'Male'


@pytest.mark.set_get
def test_user_class_remove():
    """
    Test, Checkint 'remove()' method of User Class.
    """
    user = User(36, 'Tyson', 'Fury', 'tyson@gmail.com', 'Male')
    user.remove()
    assert user.get_age() is None and user.get_name() is None and user.get_gender() is None


@pytest.mark.math
def test_revarray():
    """
    Test. Checking list reverce.
    """
    myarray = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    assertarray = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert apps.revarray(myarray) == assertarray
