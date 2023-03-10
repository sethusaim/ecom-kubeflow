import sys

from src.constant.training_pipeline import LABEL_DICT
from src.exception import EcomException


class TargetValueMapping:
    def __init__(self):
        self.dic = LABEL_DICT
        
    def get_class_mapping(self,value):
        try:
            for k, v in self.dic.items():
                if v == value:
                    return k
            return None
        
        except Exception as e:
            raise EcomException(e,sys)  
