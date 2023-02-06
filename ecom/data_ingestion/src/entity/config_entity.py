import os
from datetime import datetime

from src.constant import training_pipeline


class TrainingPipelineConfig:
    def __init__(self):
        timestamp = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

        self.pipeline_name: str = training_pipeline.PIPELINE_NAME

        self.artifact_dir: str = training_pipeline.ARTIFACT_DIR + "/" + timestamp

        self.artifact_bucket_name: str = training_pipeline.APP_ARTIFACTS_BUCKET


class DataIngestionConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.data_ingestion_dir: str = os.path.join(
            training_pipeline_config.artifact_dir,
            training_pipeline.DATA_INGESTION_DIR_NAME,
        )

        self.feature_store_dir: str = os.path.join(
            self.data_ingestion_dir, training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR
        )

        self.feature_store_file_path: str = os.path.join(
            self.feature_store_dir, training_pipeline.FILE_NAME
        )

        self.training_file_path: str = os.path.join(
            self.feature_store_dir,
            training_pipeline.TRAIN_FILE_NAME,
        )

        self.testing_file_path: str = os.path.join(
            self.feature_store_dir,
            training_pipeline.TEST_FILE_NAME,
        )

        self.train_test_split_ratio: float = (
            training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATION
        )

        self.collection_name: str = training_pipeline.DATA_INGESTION_COLLECTION_NAME
