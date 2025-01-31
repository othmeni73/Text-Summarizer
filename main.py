from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

STAGE_NAME = "data ingestion stage"
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} finished <<<<<<<<<<")
except Exception as e:
    raise e


STAGE_NAME = "data validation stage"
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<")
    data_validation=DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} finished <<<<<<<<<<")
except Exception as e:
    raise e