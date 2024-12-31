import requests
from requests.auth import HTTPDigestAuth

from shared.utils.get_config import Config
from shared.utils.logger import get_logger

logger = get_logger(__name__)


class MongodbAtlasClient:
    """Mongodb Atlas API Client"""

    def __init__(self, config: Config):
        self.config = config
        self.url = (
            f"https://{self.config.ATLAS_HOST}/{self.config.ATLAS_API_BASE_PATH}/"
        )
        self.username = self.config.ATLAS_USERNAME
        self.password = self.config.ATLAS_PASSWORD

    def get(self, endpoint: str, **kwargs) -> dict:
        """Get api call to Atlas API

        Args:
            endpoint (str): atlas api path
            kwargs (str): request call specific kwargs

        Returns:
            dict: response from atlas api
        """

        response = requests.get(
            self.url + endpoint,
            auth=HTTPDigestAuth(username=self.username, password=self.password),
            timeout=10,
            **kwargs,
        )
        data = response.json()
        return data
