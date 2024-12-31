from reports.report_base import ReportBase
from shared.data_sources.atlas import MongodbAtlasClient
from shared.utils.get_config import Config
from shared.utils.logger import get_logger

logger = get_logger(__name__)


class RecommendIndices(ReportBase):
    def __init__(self, config: Config, atlas_client: MongodbAtlasClient):
        self.config: Config = config
        self.atlas_client = atlas_client

    def report(self):
        return "test pass"
