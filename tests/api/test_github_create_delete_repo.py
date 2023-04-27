import pytest


@pytest.mark.api
def test_github_create_repo(GitHub_Api_Client):
    api_client = GitHub_Api_Client
    response = api_client.create_repo()
    
    assert response.status_code == 201


@pytest.mark.api
def test_github_delete_repo(GitHub_Api_Client):
    api_client = GitHub_Api_Client
    response = api_client.delete_repo()

    assert response.status_code == 204

