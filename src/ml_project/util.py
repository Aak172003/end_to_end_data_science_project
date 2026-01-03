import os
import sys
from src.ml_project.logger import logging
from src.ml_project.exception import CustomException
import pandas as pd
from dotenv import load_dotenv
import pymysql

# It will load all env variable
load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")


def read_sql_configuration():
    logging.info("Reading sql database")
    try:
        # Make Connection and trying to connect with sql database
        mydb = pymysql.connect(host=host, user=user, password=password, db=db)

        logging.info(f"Connection Established: {mydb}")

        df = pd.read_sql_query("Select * from student", mydb)
        print(df.head(10))
        return df

    except Exception as e:
        raise CustomException(e, sys)
