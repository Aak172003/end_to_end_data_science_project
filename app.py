from src.ml_project.logger import logging
from src.ml_project.exception import CustomException
import sys
from src.ml_project.components.data_ingestion import DataIngestion
from src.ml_project.components.data_transformation import DataTransformation
from src.ml_project.components.model_trainer import ModelTrainerConfig, ModelTrainer


if __name__ == "__main__":
    logging.info("The execution has started")

    try:
        # a = 1 / 0
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

        # Call Data Transformation
        data_transformation = DataTransformation()
        train_array, test_array, _ = data_transformation.initiate_data_transformation(
            train_data_path, test_data_path
        )

        # Model Training
        model_trainer = ModelTrainer()
        r2_score = model_trainer.initiate_model_trainer(train_array, test_array)
        print(f"R2 Score: {r2_score}")
        logging.info(f"R2 Score: {r2_score}")

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e, sys)
