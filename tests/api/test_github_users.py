import pytest
from src.libraries.helpers import text_generator


@pytest.mark.api
def test_github_get_users_per_page_default(GitHub_Api_Client):
    api_client = GitHub_Api_Client

    response = api_client.get_list_users()
    assert len(response.json()) == 30 and response.status_code == 200


@pytest.mark.api
def test_github_get_users_per_page_1(GitHub_Api_Client):
    api_client = GitHub_Api_Client
    parameters = {'per_page': 1}

    response = api_client.get_list_users(parameters)
    assert len(response.json()) == 1 and response.status_code == 200


@pytest.mark.api
def test_github_get_users_per_page_max(GitHub_Api_Client):
    api_client = GitHub_Api_Client
    parameters = {'per_page': 100}

    response = api_client.get_list_users(parameters)
    assert len(response.json()) == 100 and response.status_code == 200


@pytest.mark.api
def test_github_get_users_per_page_more_max(GitHub_Api_Client):
    api_client = GitHub_Api_Client
    parameters = {'per_page': 300}

    response = api_client.get_list_users(parameters)
    assert len(response.json()) == 100 and response.status_code == 200


@pytest.mark.api
def test_github_get_users_since_id_1000(GitHub_Api_Client):
    api_client = GitHub_Api_Client
    parameters = {'since': 1000}

    response = api_client.get_list_users(parameters)
    assert response.json()[0]['id'] == 1001 and response.status_code == 200


@pytest.mark.api
def test_github_get_users_since_id_string(GitHub_Api_Client):
    api_client = GitHub_Api_Client
    parameters = {'since': 'qwerty'}

    response = api_client.get_list_users(parameters)
    assert response.json()[0]['id'] == 1 and response.status_code == 200


@pytest.mark.api
def test_github_get_not_existing_user(GitHub_Api_Client):
    api_client = GitHub_Api_Client

    response = api_client.get_a_user(text_generator(20))
    assert response.json()["message"] == "Not Found" and response.status_code == 404


@pytest.mark.api
def test_github_get_not_existing_user(GitHub_Api_Client):
    api_client = GitHub_Api_Client
    parameters = {'subject_type': 'repository'}

    response = api_client.get_user_contextual_info(parameters)
    assert response.json() == {'contexts': []} and response.status_code == 200

