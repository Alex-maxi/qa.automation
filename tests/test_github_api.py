
import pytest
from src.libraries.helpers import text_generator
from src.application.api.parameters import Parameters
from src.application.api.github_api_client import GitHubApiClient as api


@pytest.mark.api
def test_search_repo_per_page_param_min():
    parameters = (Parameters()
                  .set_q('qa')
                  .set_per_page(1)
                  .build())
    body = api().search_repo(parameters)
    json_body = body.json()
    assert body.status_code == 200 and len(json_body["items"]) == 1


@pytest.mark.api
def test_search_repo_per_page_param_max():
    parameters = (Parameters()
                  .set_q('qa')
                  .set_per_page(100)
                  .build())
    body = api().search_repo(parameters)
    json_body = body.json()
    assert body.status_code == 200 and len(json_body["items"]) == 100


@pytest.mark.api
def test_search_repo_per_page_param_sort_order():
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
    body_asc = api().search_repo(parameters_asc).json()
    body_desc = api().search_repo(parameters_desc).json()
    assert body_asc["items"] == body_desc["items"][::-1]


@pytest.mark.api
def test_search_repo_no_such_repo():
    repo_name = text_generator(30)
    parameters = Parameters().set_q(repo_name).build()
    body = api().search_repo(parameters)
    body_json = body.json()
    assert body.status_code == 200 and body_json["total_count"] == 0

