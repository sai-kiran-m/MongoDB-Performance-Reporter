from reports.factories.report_factory import ReportFactoryBase
from reports.recommend_indices import RecommendIndices
from shared.data_sources.atlas import MongodbAtlasClient
from shared.utils.get_config import Config


class RecommendIndicesFactory(ReportFactoryBase):
    def __init__(self, config: Config):
        self.config: Config = config
        self.atlas_client = MongodbAtlasClient(config)

    def create_report(self) -> RecommendIndices:
        return RecommendIndices(self.config, self.atlas_client)
