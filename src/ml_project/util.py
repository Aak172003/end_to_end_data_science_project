import os
import sys
from src.ml_project.logger import logging
from src.ml_project.exception import CustomException
import pandas as pd
from dotenv import load_dotenv
import pymysql
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score


import pickle
import numpy as np

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


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)


# This function is used to evaluate the models and find the best model among them based on r2_score
# It will return a report which contains the name of the model and its r2_score on test data

def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para = param[list(models.keys())[i]]

            gs = GridSearchCV(model, para, cv=3)
            gs.fit(X_train, y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)

            # model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)
