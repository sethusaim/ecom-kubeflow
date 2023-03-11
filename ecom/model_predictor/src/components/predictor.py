import sys

from src.cloud_storage.aws_storage import S3Operation
from src.entity.config_entity import PredictionConfig
from src.exception import EcomException
from src.logger import logging
from src.ml.feature import text_normalizer
from src.ml.model.estimator import TargetValueMapping
from src.utils.main_utils import load_object
import nltk


class Predictor:
    def __init__(self):
        self.prediction_config = PredictionConfig()

        self.s3 = S3Operation()

        nltk.download("stopwords")

    def get_prediction(self, text):
        logging.info("Entered get_prediction method of Predictor class")

        try:
            self.s3.sync_folder_from_s3(
                folder=self.prediction_config.config_folder,
                bucket_name=self.prediction_config.config_bucket_name,
                bucket_folder_name=self.prediction_config.config_folder,
            )

            self.s3.sync_folder_from_s3(
                folder=self.prediction_config.model_folder,
                bucket_name=self.prediction_config.config_bucket_name,
                bucket_folder_name=self.prediction_config.model_folder,
            )

            model = load_object(file_path=self.prediction_config.model_file_name)

            logging.info("Loaded model for predictions")

            normalized_text: str = text_normalizer(
                text=text,
                acronyms_dict_path=self.prediction_config.data_transformation_acronyms_file_path,
                contractions_dict_path=self.prediction_config.data_transformation_contraction_file_path,
            )

            preds = model.predict(normalized_text)[0]

            logging.info("Got the model predictions")

            preds_mapping = TargetValueMapping().get_class_mapping(value=preds)

            logging.info("Applied target value mapping in predictions")

            logging.info("Exited get_prediction method of Predictor class")

            return preds_mapping

        except Exception as e:
            raise EcomException(e, sys)
