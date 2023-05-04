from src.config.providers.base_config import BaseConfigKeyProvider


# BaseConfigKeyProvider usage is optional
class ConfigFromDefaultsProvider(BaseConfigKeyProvider):
    """
    Allows default configuration.
    Args:
        BaseConfigKeyProvider (class): Base configuration class
    """

    def __init__(self, props) -> None:
        self.props = props

    def get(self, key):
        """
        Returns config value for the given key
        :param str key: Key to retrieve
        """
        return self.props.get(key)