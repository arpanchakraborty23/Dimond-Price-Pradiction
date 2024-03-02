import os
import sys
from src.logger import logging
from src.exception import CustomException
from src.components.data_transformation import DataTransformation,DataTransformationconfig
from src.components.model_trainer import ModelTrainer,ModelTrainerConfig

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


## intialize the data ingestion configuration

@dataclass
class DataIngestionconfig:
    train_data_path=os.path.join('artifacts','train.csv')
    test_data_path=os.path.join('artifacts','test.csv')
    raw_data_path=os.path.join('artifacts','raw.csv')


## create a data ingestion class
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionconfig()

    def initiate_data_ingestion(self):
        logging.info('Data Ingestion method starts')

        try:
            df=pd.read_csv(os.path.join('notebooks/data','gemstone.csv'))
            logging.info('Dataset read as pandas Dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False)

            logging.info("Train test split")
            train_set,test_set=train_test_split(df,test_size=0.30,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('Ingestion of data is completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )



        except Exception as e:
            logging.info('Error occured in Data Ingestion config')

if __name__=='__main__':

    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    obj_data=DataTransformation()
    train_arr,test_arr,_=obj_data.initiate_data_transformation(train_data,test_data)

    obj_model=ModelTrainer()
    print(obj_model.initiate_model_trainer(train_arr,test_arr))
    






