import sys,os

from sklearn import preprocessing
from housing.exception import HousingException
from housing.logger import logging
from housing.entity.config_entity import  DataTransformationConfig
from housing.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
import numpy as np
from sklearn.base import BaseEstimator,TransformerMixin
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
import pandas as pd
from housing.util.util import read_yaml_file
from housing.constant import *




class FeatureGenerator(BaseEstimator,TransformerMixin):
    def __init__(self,add_bedrooms_per_room = True,total_rooms_ix = 3,population_ix=5,households_ix = 6,total_bedrooms_ix =4, columns= None):
        """
        FeatureGenerator Initialialization
        add_bedrooms_per_room:bool
        total_rooms_ix: int index number of total rooms columns
        population_ix: int index number of total population columns
        households_ix = int index number of households columns
        toal_bedrooms_ix: int index number fo bedrooms columns

        """
   
        try:
            self.columns= columns
            if self.columns is not None:
                total_rooms_ix = self.columns.index(COLUMN_TOTAL_ROOMS)
                population_ix = self.columns.index(COLUMN_POPULATION)
                households_ix = self.columns.index(COLUMN_HOUSEHOLDS)
                total_bedrooms_ix = self.columns.index(COLUMN_TOTAL_BEDROOM)

            self.add_bedrooms_per_room = add_bedrooms_per_room
            self.total_rooms_ix =total_rooms_ix
            self.population_ix = population_ix
            self.households_ix = households_ix
            self.total_bedrooms_ix = total_bedrooms_ix

        except Exception as e:
            raise HousingException(e,sys) from e

    def fit(self,X,y=None):

        return self

    def transform(self,X,y=None):
        try:
            room_per_household = X[:,self.total_rooms_ix] / \
                                 X[:,self.households_ix]

            population_per_households = X[:,self.population_ix] /\
                                        X[:,self.households_ix]

            if self.add_bedrooms_per_room:
                bedroom_per_room = X[:,self.total_bedrooms_ix] /\
                                   X[:,self.total_rooms_ix]

                generate_feature = np.c_[X,room_per_household,population_per_households,bedroom_per_room]
            else:
                generate_feature = np.c_[X,room_per_household,population_per_households]

            return generate_feature
        except Exception as e:
            raise HousingException(e,sys) from e

class DataTransformation:
    def __init__(self,data_transformation_config: DataTransformationConfig,
                data_ingestion_artifact : DataIngestionArtifact,
                data_validation_artifact: DataValidationArtifact
                ):
        try:
           self.data_transformation_config = data_transformation_config
           self.data_ingestion_artifact = data_ingestion_artifact
           self.data_validation_artifact = data_validation_artifact 
        except Exception as e:
            raise HousingException(e,sys) from e

    @staticmethod
    def load_data(file_path:str,schema_file_path:str) -> pd.DataFrame:
        try:
            dataset_schema = read_yaml_file(schema_file_path)
            schema = dataset_schema[DATASET_SCHEMA_COLUMNS_KEY]
            dataframe = pd.read_csv(file_path)
            error_message = ""
            
            for column in dataframe.columns:
                if column in list(schema.keys()):
                    dataframe[column].astype(schema[column])
                else:
                    error_message = f"{error_message} \nColumn: [{column}] is not in the schema."

            if len(error_message) >0:
                raise Exception(error_message)
            return dataframe

        except Exception as e:
            raise HousingException(e,sys) from e

    def get_data_transformer_oject(self)->ColumnTransformer:
        try:
            schema_file_path = self.data_validation_artifact.schema_file_path
            dataset_schema = read_yaml_file(file_path=schema_file_path)
            numerical_columns = dataset_schema[NUMERICAL_COLUMN_KEY]
            categorical_columns = dataset_schema[CATEGORICAL_COLUMN_KEY]

            num_pipeline = Pipeline(steps=[
                ("imputer",SimpleImputer(strategy="median")),
                ("feature_generator",FeatureGenerator(
                    add_bedrooms_per_room=self.data_transformation_config.add_bedroom_per_room,columns=numerical_columns)),
                ('scaler',StandardScaler())
            ])

            cat_pipeline = Pipeline(steps=[
                ('impute',SimpleImputer(strategy='most_frequent')),
                ('one_hot_encoder',OneHotEncoder()),
                ('scaler',StandardScaler(with_mean=False))
            ])

            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")

            preprocessing = ColumnTransformer([('num_pipeline',num_pipeline,numerical_columns),('cat_pipeline',cat_pipeline,categorical_columns)])

            return preprocessing

        except Exception as e:
            raise HousingException(e,sys) from e




     


