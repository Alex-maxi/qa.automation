import pytest
from src.application.utitapp.app import Apps
from src.application.api.github_api_client import GitHubApiClient
from src.libraries.helpers import read_data_from_csv
from src.config.config import config
from src.data.models.users import User


url = config.get('BASE_URL_API')
input_data = config.get("TEST_DATA")
sum_test_data = read_data_from_csv(input_data)
apps = Apps()
api = GitHubApiClient()

# Test with using DDT


@pytest.mark.math
@pytest.mark.parametrize("data, result", sum_test_data)
def test_api_git_2(data, result):
    assert apps.get_sum_of_digits(data) == int(result)

# Testing User class


@pytest.mark.set_get
def test_user_age_and_name_dict():
    user = User().set_name('Tyson').set_age(36).set_lastname('Fury').set_email(
        'tyson@gmail.com').set_gender('Male').build_user_obj()
    assert user['age'] == 36 and user['name'] == "Tyson" and user['email'] == 'tyson@gmail.com'

# Testing User class


@pytest.mark.set_get
def test_user_age_and_name_class():
    user = User(36, 'Tyson', 'Fury', 'tyson@gmail.com', 'Male')
    assert user.get_age() == 36 and user.get_name(
    ) == "Tyson" and user.get_gender() == 'Male'

# Testing User class


@pytest.mark.set_get
def test_user_class_remove():
    user = User(36, 'Tyson', 'Fury', 'tyson@gmail.com', 'Male')
    user.remove()
    assert user.get_age() == None and user.get_name(
    ) == None and user.get_gender() == None

# Testing arr reverce


@pytest.mark.math
def test_revarray():
    myarray = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    assertarray = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert apps.revarray(myarray) == assertarray
