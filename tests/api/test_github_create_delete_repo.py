"""The `pytest` module provides a testing framework for Python"""
import pytest


@pytest.mark.api
def test_github_create_repo(github_api_client):
    """Positive Test for creatint GitHub repo"""
    api_client = github_api_client
    response = api_client.create_repo()

    assert response.status_code == 201


@pytest.mark.api
def test_github_delete_repo(github_api_client):
    """Positive Test for deleting GitHub repo"""
    api_client = github_api_client
    response = api_client.delete_repo()

    assert response.status_code == 204
