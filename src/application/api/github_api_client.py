import requests
from src.config.config import CONFIG


class GitHubApiClient:

    def __init__(self) -> None:
        self.token = None

    def search_repo(self, parameters):
        response = requests.get(
            url=self._form_url("/search/repositories"),
            params=parameters,
            # headers=f"Authorization: Bearer {self.token}"
        )
        return response

    def login(self, username, password):
        print(f"Do login with {username}:{password}")
        self.token = "sdkfjbkjsdf"

    def logout(self):
        print("Do logout for")

    def _form_url(self, url):
        return CONFIG.get("BASE_URL_API") + url
