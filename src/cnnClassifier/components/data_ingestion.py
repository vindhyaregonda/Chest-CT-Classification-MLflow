import os
import urllib.request as request
import zipfile
import gdown
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config

    def download_file(self):
        '''Fetches data from the url'''

        try:
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logger.info(f"Downloading data from {dataset_url} to {zip_download_dir}")

            fileid = dataset_url.split("/")[-2]
            prefix = "https://drive.google.com/uc?/export=download&id="
            gdown.download(prefix + fileid, zip_download_dir)

            logger.info(f"Downloaded data to {zip_download_dir}")

        except Exception as e:
            # logger.error(f"Error downloading data: {e}")
            raise e
        
    def extract_zip_file(self):
        """ 
        zip_file: Path to the zip file
        Extracts the zip file to the directory
        Function return None
        """

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

