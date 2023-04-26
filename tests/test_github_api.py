import pytest
from src.libraries.helpers import text_generator
from src.application.api.parameters import Parameters
from src.config.config import CONFIG


@pytest.mark.api
def test_search_repo_per_page_param_min(GitHub_Api_Client):
    api_client = GitHub_Api_Client
    parameters = (Parameters()
                  .set_q('qa')
                  .set_per_page(1)
                  .build())
    body = api_client.search_repo(parameters)
    json_body = body.json()
    assert body.status_code == 200 and len(json_body["items"]) == 1


@pytest.mark.api
def test_search_repo_per_page_param_max(GitHub_Api_Client):
    api_client = GitHub_Api_Client
    parameters = (Parameters()
                  .set_q('qa')
                  .set_per_page(100)
                  .build())
    body = api_client.search_repo(parameters)
    json_body = body.json()
    assert body.status_code == 200 and len(json_body["items"]) == 100


@pytest.mark.api
def test_search_repo_per_page_param_sort_order(GitHub_Api_Client):
    api_client = GitHub_Api_Client
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
def test_search_repo_no_such_repo(GitHub_Api_Client):
    api_client = GitHub_Api_Client
    repo_name = text_generator(30)
    parameters = Parameters().set_q(repo_name).build()
    body = api_client.search_repo(parameters)
    body_json = body.json()
    assert body.status_code == 200 and body_json["total_count"] == 0

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

