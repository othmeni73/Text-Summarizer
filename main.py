from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "data ingestion stage"
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} finished <<<<<<<<<<")
except Exception as e:
    raise e 