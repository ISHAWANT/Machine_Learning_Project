from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logger import logging
from housing.config.configuration import Configuration
from housing.component.data_transformation import DataTransformation

def main():
    try:
        # pipeline = Pipeline()
        # pipeline.run_pipeline()
        # data_validation_config = Configuration().get_data_transformation_config()
        # print(data_validation_config)
        schema_file_path = r"E:\avnish_proj\Machine_Learning_Project\config\schema.yaml"
        file_path = r"E:\avnish_proj\Machine_Learning_Project\housing\artifact\data_ingestion\2022-09-21-20_04-09\ingested_data\train\housing.csv"
        df = DataTransformation.load_data(file_path=file_path,schema_file_path=schema_file_path)
        print(df.columns)
        print(df.dtypes)

    except Exception as e:
        logging.error(f"{e}")
        print(e)



if __name__=="__main__":
    main()

