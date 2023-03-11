import os

from src.constant import training_pipeline


class PredictionConfig:
    def __init__(self):
        self.config_folder: str = training_pipeline.DATA_TRANSFORMATION_CONFIG_FOLDER

        self.model_folder: str = training_pipeline.BEST_MODEL_FOLDER

        self.model_file_name: str = os.path.join(
            self.model_folder, training_pipeline.BEST_MODEL_FILE_NAME
        )

        self.config_bucket_name: str = (
            training_pipeline.DATA_TRANSFORMATION_CONFIG_BUCKET_NAME
        )

        self.data_transformation_acronyms_file_path: str = os.path.join(
            self.config_folder,
            training_pipeline.DATA_TRANSFORMATION_ACRONYMS_CONFIG_FILE,
        )

        self.data_transformation_contraction_file_path: str = os.path.join(
            self.config_folder,
            training_pipeline.DATA_TRANSFORMATION_CONTRACTIONS_CONFIG_FILE,
        )
