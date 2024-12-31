import argparse

from reports.factories.recommend_indices_factory import RecommendIndicesFactory
from reports.factories.report_factory import ReportFactoryBase
from reports.report_base import ReportBase
from shared.utils.get_config import Config
from shared.utils.logger import get_logger

logger = get_logger(__name__)
FACTORY_MAP = {"recommend_indices": RecommendIndicesFactory}

parser = argparse.ArgumentParser(
    prog="A Mongodb Performance Reporter App",
    description="This app will help you to recieve emails reports related to"
    "mongodb collections and their performance.",
)
parser.add_argument("--report_name", help="Provide the name of report")

if __name__ == "__main__":
    args = parser.parse_args()
    logger.info(f"Recieved input args {args.__dict__}")
    report_name = args.report_name

    config: Config = Config()
    report_factory: ReportFactoryBase = FACTORY_MAP[report_name](config)
    report: ReportBase = report_factory.create_report()
    report.report()
