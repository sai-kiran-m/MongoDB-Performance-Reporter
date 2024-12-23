import json
import os

CONFIG_FOLDER = os.path.join(os.path.dirname(__file__), "../../../config")


class Config:
    def __init__(self):
        # self.vars: dict = {}
        self.env = os.getenv("ENV") or "nonprod"
        file_name = f"{self.env}.json"
        config_file_path = os.path.join(CONFIG_FOLDER, file_name)

        with open(config_file_path, "r") as file:
            config_data: dict = json.load(file)
            for key, val in config_data.items():
                setattr(self, key, val)
        self.ATLAS_USERNAME = os.getenv("ATLAS_USERNAME")
        self.ATLAS_PASSWORD = os.getenv("ATLAS_PASSWORD")
