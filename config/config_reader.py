import yaml
from pathlib import Path


class ConfigReader:

    @staticmethod
    def read_config():

        config_path = Path("config/config.yaml")

        with open(config_path) as file:
            return yaml.safe_load(file)


    @staticmethod
    def read_environment():

        config = ConfigReader.read_config()
        env = config["environment"]

        env_path = Path("config/environments.yaml")

        with open(env_path) as file:
            env_data = yaml.safe_load(file)

        return env_data[env]