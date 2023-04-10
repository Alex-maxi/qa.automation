import requests
from src.config.config import config


class GitHubApiClient:

    def __init__(self) -> None:
        self.token = None

    def get_method(self, arg):
        response = requests.get(arg)
        return response

    def search_repo(self, repo_name):
        r = requests.get(
            url=self._form_url("/search/repositories"),
            params={'q': repo_name},
            # headers=f"Authorization: Bearer {self.token}"
        )

        return r.json()

    def login(self, username, password):
        print(f"Do login with {username}:{password}")
        self.token = "sdkfjbkjsdf"

    def logout(self):
        print("Do logout for")

    def _form_url(self, url):
        return config.get("BASE_URL_API") + url
