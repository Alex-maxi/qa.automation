import os
from src.config.providers.config_from_defults_provider import ConfigFromDefaultsProvider
from src.config.providers.config_from_env_provider import ConfigFromEnvProvider
from src.config.providers.config_from_json_provider import ConfigFromSimpleJsonProvider


class Config:
    default_env = "dev"

    def __init__(self) -> None:
        self.conf_dict = {}

        target = os.environ.get('TARGET')
        if target is None:
            target = Config.default_env

        json_path = f"src/config/env_config/{target}.json"
        json_path_auth = f"src/config/env_config/data_auth.json"

        # Hierarhy of providers
        self.providers = [
            ConfigFromDefaultsProvider({
                "DEBUG_MODE": False,
                "BROWSER": 'chrome',
                "UI_TIMEOUTS": 30,
                "SELENIUM_GRID_URL": 'http://192.168.31.88:4444/wd/hub'
            }),
            ConfigFromSimpleJsonProvider(json_path),
            ConfigFromSimpleJsonProvider(json_path_auth),
            ConfigFromEnvProvider()
            ]

        self.register("BASE_URL_API")
        self.register("BASE_URL_UI")
        self.register("TEST_DATA")
        self.register("BROWSER")
        self.register("DEBUG_MODE")
        self.register("UI_TIMEOUTS")
        self.register("GIT_HUB_TOKEN")
        self.register("SELENIUM_GRID_URL")
        

        
    def register(self, name):
        """
        Register name of the key which is used
        in tests
        """

        # Order in self.provider makes difference
        for provider in self.providers:
            val = provider.get(name)

            if val is not None:
                self.conf_dict[name] = val

        # raise error if no value is found across the providers
        val = self.conf_dict.get(name)
        if val is None:    
            raise Exception(f"{name} variable is not set in config")

        print(f"{name} variable is registered in config with value {val}")

    def get(self, name):
        """
        Return existing value
        """
        val = self.conf_dict.get(name)
        if val is None:    
            raise Exception(f"{name} variable is not set in config")

        return self.conf_dict.get(name)


# python way singleton
CONFIG = Config()