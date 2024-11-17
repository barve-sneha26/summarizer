from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.st_1_data_ingestion_pipeline import DataIngestionPipeline 

# logger.info("Logging is implemented")

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"Stage {STAGE_NAME} initiated") 
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"Stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e 
