from reports.factories.report_factory import ReportFactoryBase
from reports.recommend_indexes import RecommendIndexes
from shared.data_sources.atlas import MongodbAtlasClient
from shared.utils.get_config import Config


class RecommendIndexesFactory(ReportFactoryBase):
    def __init__(self, config: Config):
        self.config: Config = config
        self.atlas_client = MongodbAtlasClient(config)

    def create_report(self) -> RecommendIndexes:
        return RecommendIndexes(self.config, self.atlas_client)
