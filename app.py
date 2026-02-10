from src.ml_project.logger import logging
from src.ml_project.exception import CustomException
import sys
from src.ml_project.components.data_ingestion import DataIngestion
from src.ml_project.components.data_transformation import DataTransformation


if __name__ == "__main__":
    logging.info("The execution has started")

    try:
        # a = 1 / 0
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

        # Call Data Transformation
        data_transformation = DataTransformation()
        data_transformation.initiate_data_transformation(
            train_data_path, test_data_path
        )
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e, sys)
