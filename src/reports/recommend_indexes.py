from reports.report_base import ReportBase
from shared.data_sources.atlas import MongodbAtlasClient
from shared.utils.get_config import Config


class RecommendIndexes(ReportBase):
    def __init__(self, config: Config, atlas_client: MongodbAtlasClient):
        self.config: Config = config
        self.atlas_client = atlas_client

    def report(self):
        # for each team parse through their namespace
        # intellengent parsing
            # identity cluster
            # pull suggested indexes on the cluster with its primary shard details 
        return "test pass"
