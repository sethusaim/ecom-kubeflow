import json
import pickle
import sys

from src.exception import EcomException


def load_object(file_path: str):
    try:
        with open(file_path, "rb") as f:
            file_obj = pickle.load(f)

        return file_obj

    except Exception as e:
        raise EcomException(e, sys)


def read_json(file_path: str):
    try:
        with open(file=file_path, mode="r") as f:
            dic = json.load(f)

        return dic

    except Exception as e:
        raise EcomException(e, sys)
