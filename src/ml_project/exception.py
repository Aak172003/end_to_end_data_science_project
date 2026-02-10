import sys
from src.ml_project.logger import logging


def error_message_details(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    print("_, _, exc_tb ::::: ", _, _, exc_tb)
    file_name = exc_tb.tb_frame.f_code.co_filename
    print("this will give filename ", file_name)
    # preparing error message
    error_message = "Error occurred python script name [{0}] line number [{1}] error message [{2}].".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message


class CustomException(Exception):
    # Initialization contructor
    def __init__(self, error_message, error_details: sys):
        # inheriotence all properties and methods of Exception
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_details)

    def __str__(self):
        return self.error_message
