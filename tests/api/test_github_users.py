"""The `pytest` module provides a testing framework for Python"""
import pytest
from src.libraries.helpers import text_generator


@pytest.mark.api
def test_github_get_users_per_page_default(github_api_client):
    """Getting list of users by default."""
    api_client = github_api_client

    response = api_client.get_list_users()
    assert len(response.json()) == 30 and response.status_code == 200


@pytest.mark.api
def test_github_get_users_per_page_1(github_api_client):
    """Getting list of users '1' per page."""
    api_client = github_api_client
    parameters = {'per_page': 1}

    response = api_client.get_list_users(parameters)
    assert len(response.json()) == 1 and response.status_code == 200


@pytest.mark.api
def test_github_get_users_per_page_max(github_api_client):
    """Getting list of users max value, '100' per page."""
    api_client = github_api_client
    parameters = {'per_page': 100}

    response = api_client.get_list_users(parameters)
    assert len(response.json()) == 100 and response.status_code == 200


@pytest.mark.api
def test_github_get_users_per_page_more_max(github_api_client):
    """Getting list of users by setting per page parameter above max value, '100' per page."""
    api_client = github_api_client
    parameters = {'per_page': 300}

    response = api_client.get_list_users(parameters)
    assert len(response.json()) == 100 and response.status_code == 200


@pytest.mark.api
def test_github_get_users_since_id_1000(github_api_client):
    """Getting list of users after id 1000"""
    api_client = github_api_client
    parameters = {'since': 1000}

    response = api_client.get_list_users(parameters)
    assert response.json()[0]['id'] == 1001 and response.status_code == 200


@pytest.mark.api
def test_github_get_users_since_id_string(github_api_client):
    """Getting list of users. Setting 'since_id' like string"""
    api_client = github_api_client
    parameters = {'since': 'qwerty'}

    response = api_client.get_list_users(parameters)
    assert response.json()[0]['id'] == 1 and response.status_code == 200


@pytest.mark.api
def test_github_get_not_existing_user(github_api_client):
    """Getting list of not existing user"""
    api_client = github_api_client

    response = api_client.get_a_user(text_generator(20))
    assert response.json()["message"] == "Not Found" and response.status_code == 404


@pytest.mark.api
def test_github_get_existing_user(github_api_client):
    """Getting authorized user"""
    api_client = github_api_client
    parameters = {'subject_type': 'repository'}

    response = api_client.get_user_contextual_info(parameters)
    assert response.json() == {'contexts': []} and response.status_code == 200
