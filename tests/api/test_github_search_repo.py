"""The `pytest` module provides a testing framework for Python"""
import pytest
from src.application.api.search_repo_parameters import SearchRepoParameters as Parameters
from src.libraries.helpers import text_generator


@pytest.mark.api
def test_search_repo_per_page_param_min(github_api_client):
    """Positive test case with minimum per page query param '1'"""
    api_client = github_api_client

    parameters = (Parameters()
                  .set_q('qa')
                  .set_per_page(1)
                  .build())

    body = api_client.search_repo(parameters)
    json_body = body.json()

    assert body.status_code == 200 and len(json_body["items"]) == 1


@pytest.mark.api
def test_search_repo_per_page_param_max(github_api_client):
    """Positive test case with maximum per page query param '100'"""
    api_client = github_api_client

    parameters = (Parameters()
                  .set_q('qa')
                  .set_per_page(100)
                  .build())

    body = api_client.search_repo(parameters)
    json_body = body.json()

    assert body.status_code == 200 and len(json_body["items"]) == 100


@pytest.mark.api
def test_search_repo_per_page_param_sort_order(github_api_client):
    """Positive test case 'desc' and 'asc' sorting"""
    api_client = github_api_client

    parameters_asc = (Parameters()
                      .set_q('sokolov+language:python')
                      .set_sort("updated")
                      .set_order("desc")
                      .build())
    parameters_desc = (Parameters()
                       .set_q('sokolov+language:python')
                       .set_sort("updated")
                       .set_order("asc")
                       .build())

    body_asc = api_client.search_repo(parameters_asc).json()
    body_desc = api_client.search_repo(parameters_desc).json()

    assert body_asc["items"] == body_desc["items"][::-1]


@pytest.mark.api
def test_search_repo_no_such_repo(github_api_client):
    """Positive test case searching not existing repo"""
    api_client = github_api_client
    repo_name = text_generator(30)
    parameters = Parameters().set_q(repo_name).build()

    body = api_client.search_repo(parameters)
    body_json = body.json()

    assert body.status_code == 200 and body_json["total_count"] == 0
