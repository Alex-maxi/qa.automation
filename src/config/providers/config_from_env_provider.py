import os
from src.config.providers.base_config import BaseConfigKeyProvider


# BaseConfigKeyProvider usage is optional
class ConfigFromEnvProvider(BaseConfigKeyProvider):
    """
    Allows configuration through the env variables.
    Args:
        BaseConfigKeyProvider (class): Base config class
    """
    def get(self, key):
        """
        Returns config value for the given key
        :param str key: Key to retrieve
        """

        print('Config From Env Provider')
        print(os.environ.get(key))

        return os.environ.get(key)
