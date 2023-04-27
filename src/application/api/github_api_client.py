import requests
from src.config.config import CONFIG
from src.libraries.helpers import text_generator


class GitHubApiClient:

    def __init__(self) -> None:
        self.token = None
        self.owner = None
        self.repo_name = None


    def search_repo(self, parameters):
        response = requests.get(
            url=self._form_url("/search/repositories"),
            params=parameters,
            headers = {"Authorization": f"Bearer {self.token}"}
        )
        return response
    

    def create_repo(self):
        url = self._form_url("/user/repos")
        headers = {"Authorization": f"Bearer {self.token}"}
        data = {
            "name": text_generator(30),
            "description": "This is repo created using API!",
            "private": False,
        }
        response = requests.post(url, headers=headers, json=data)
        self.repo_name = response.json()['name']
        return response


    def delete_repo(self):
        url = self._form_url(f"/repos/{self.owner}/{self.repo_name}")
        headers = {'Authorization': f'token {self.token}'}
        response = requests.delete(url, headers=headers)
        return response


    def login(self):
        self.token = CONFIG.get("GIT_HUB_TOKEN")
        headers = {
            'Authorization': f'token {self.token}',
            'Accept': 'application/vnd.github+json',
            'X-GitHub-Api-Version': '2022-11-28'
        }
        response = requests.get(f'{self._form_url("/user")}', headers=headers)
        self.owner = response.json()['login']


    def logout(self):
        self.token = None
        self.owner = None
        self.owner_repo_url = None


    def _form_url(self, url):
        return CONFIG.get("BASE_URL_API") + url
