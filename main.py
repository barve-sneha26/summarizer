from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.st1_data_ingestion_pipeline import DataIngestionPipeline
from src.textSummarizer.pipeline.st2_data_transformation_pipeline import DataTransformationPipeline 
from src.textSummarizer.pipeline.st3_model_trainer_pipeline import ModelTrainerPipeline
from src.textSummarizer.pipeline.st4_model_evaluation_pipeline import ModelEvaluationPipeline 
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

STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f"Stage {STAGE_NAME} initiated") 
    data_ingestion_pipeline = DataTransformationPipeline()
    data_ingestion_pipeline.initiate_data_transformation() 
    logger.info(f"Stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e 


STAGE_NAME="Model Trainer stage"

try:
    logger.info(f"stage {STAGE_NAME} initiated")
    model_trainer_pipeline=ModelTrainerPipeline()
    model_trainer_pipeline.initiate_model_trainer()
    logger.info(f"Stage {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation stage"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evaluation = ModelEvaluationPipeline()
   model_evaluation.initiate_model_evaluation()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e 