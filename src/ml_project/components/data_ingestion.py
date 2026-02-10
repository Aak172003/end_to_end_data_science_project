# Read Datasets from MYSQL
# Perform Train and Test Split on Data
# Store Train and Test split data in local

import os
import sys
from src.ml_project.logger import logging
from src.ml_project.exception import CustomException
import pandas as pd
from src.ml_project.util import read_sql_configuration
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "raw.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        """
        Fetch the data sets from the mysql database
        """
        try:
            # Pass -> means if we have no execution line so just write pass
            # pass

            # Reading code
            # df = read_sql_configuration()

            # ---------------------------------------------------------------------------------------------------------

            # Read data from csv file instead of reading every time from sql database
            df = pd.read_csv(os.path.join("notebook/data", "raw.csv"))
            logging.info("Reading completed from sql database")

            os.makedirs(
                os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True
            )

            # It will convert to csv and store to raw.csv file
            # And add index=Flase , it means it will not read indexs
            # And add header=True , make sure reads the headers
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(
                self.ingestion_config.train_data_path, index=False, header=True
            )
            test_set.to_csv(
                self.ingestion_config.test_data_path, index=False, header=True
            )

            logging.info("Data Ingestion is completed ")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )
        except Exception as e:
            raise CustomException(e, sys)
