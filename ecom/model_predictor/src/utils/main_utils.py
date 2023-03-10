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
