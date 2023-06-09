import sys

from src.exception import EcomException


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
