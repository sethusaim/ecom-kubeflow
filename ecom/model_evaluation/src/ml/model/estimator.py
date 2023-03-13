import os
import sys
from typing import Union

import boto3

from src.cloud_storage.aws_storage import S3Operation
from src.exception import EcomException
from src.logger import logging

s3 = S3Operation()


def is_model_present(model_path: str, bucket_name: str) -> bool:
    try:
        s3_resource = boto3.resource("s3")

        bucket = s3_resource.Bucket(bucket_name)

        file_objects = [
            file_object for file_object in bucket.objects.filter(Prefix=model_path)
        ]

        if len(file_objects) > 0:
            return True

        else:
            return False

    except Exception as e:
        raise EcomException(e, sys)


def get_s3_model(model_path: str, bucket_name: str) -> Union[str, None]:
    try:
        model_dir: str = os.path.dirname(model_path)

        logging.info(f"Got model dir")

        if is_model_present(model_path=model_path, bucket_name=bucket_name) is True:
            logging.info("Best model is present, downloading it")

            s3.sync_folder_from_s3(
                folder=model_dir,
                bucket_name=bucket_name,
                bucket_folder_name=model_dir,
            )

            logging.info("Downloaded best model from s3 bucket")

            return model_path

        else:
            logging.info("Best model not found in s3 bucket")

            return None

    except Exception as e:
        raise EcomException(e, sys)


class EcomModel:
    def __init__(self, preprocessor, model):
        try:
            self.preprocessor = preprocessor

            self.model = model

        except Exception as e:
            raise EcomException(e, sys)

    def predict(self, x):
        try:
            x_transform = self.preprocessor.transform(x)

            y_hat = self.model.predict(x_transform)

            return y_hat

        except Exception as e:
            raise EcomException(e, sys)
