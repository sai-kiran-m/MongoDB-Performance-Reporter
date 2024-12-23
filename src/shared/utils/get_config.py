import json
import os

CONFIG_FOLDER = os.path.join(os.path.dirname(__file__), "../../../config")


class Config:
    def __init__(self):
        env = os.getenv("ENV") or "nonprod"
        file_name = f"{env}.json"
        self.config_file_path = os.path.join(CONFIG_FOLDER, file_name)
        self._load_config()

    def _load_config(self):
        with open(self.config_file_path, "r") as file:
            self._config_data: dict = json.load(file)
        self._config_data["ATLAS_USERNAME"] = os.getenv("ATLAS_USERNAME")
        self._config_data["ATLAS_PASSWORD"] = os.getenv("ATLAS_PASSWORD")

    def __getattr__(self, name):
        if name in self._config_data:
            return self._config_data[name]
        else:
            raise AttributeError(f"Config has no attribute '{name}'")
