import os
import sys

from src.exception import EcomException


class S3Operation:
    def sync_folder_from_s3(
        self, folder: str, bucket_name: str, bucket_folder_name: str
    ) -> None:
        try:
            os.system(f"aws s3 sync s3://{bucket_name}/{bucket_folder_name}/ {folder}")

        except Exception as e:
            raise EcomException(e, sys)
