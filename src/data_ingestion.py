import os
import pandas as pd
from google.cloud import storage
from src.logger import get_logger
from src.custom_exception import CustomException
from config.paths_config import *
from utils.common_functions import read_yaml


logger = get_logger(__name__)

class DataIngestion:
    def __init__(self,config):
        self.config=config['data_ingestion']
        self.bucket_name=self.config['bucket_name']
        self.file_names=self.config['bucket_file_names']

        os.makedirs(RAW_DIR,exist_ok=True)
        logger.info("Dat Ingestion started")
    
    def download_csv_from_gcp(self):
        try:
            client = storage.Client()
            bucket = client.bucket(self.bucket_name)

            for file_name in self.file_names:
                file_path=os.path.join(RAW_DIR,file_name)

                if file_name=="animelist.csv":
                    blob = bucket.blob(file_name)
                    blob.download_to_filename(file_path)
                    data=pd.read_csv(file_path,nrows=500)
                    data.to_csv(file_path,index=False)
                    logger.info("Large file detected only donwloading 5M rows")

                else:
                    blob=bucket.blob(file_name)
                    blob.download_to_filename(file_path)
                    logger.info("Downloading other two small files")
            
        except Exception as e: 
            logger.error(f"Error occurred while downloading data from GCP: {e}")
            raise CustomException("Error occurred while downloading data from GCP",e)
        
    def run(self):
        try:
            logger.info("Starting Data ingestion")
            self.download_csv_from_gcp()
            logger.info("Data ingestion completed successfully")
        except Exception as e:
            logger.error(f"Error occurred while running Data ingestion: {e}")
            raise CustomException("Error occurred while running Data ingestion",e)
        finally:
            logger.info("Data Ingestion Done....")
                
if __name__ == "__main__":
    data_ingestion=DataIngestion(read_yaml(CONFIG_PATH))
    data_ingestion.run()
