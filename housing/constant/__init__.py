

import os
from datetime import datetime
from tkinter import CURRENT

ROOT_DIR = os.getcwd()  #to get current working directory

CONFIG_DIR = "config"

CONFIG_FILE_NAME = "config.yaml"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILE_NAME)

CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H_%M-%S')}"

#Training pipeline related  variable

TRAINING_PIPELINE_CONFIG_KEY = "training_pipeline_config"
TRAINING_PIPELINE_ARTIFACT_DIR_KEY = "artifact_dir"
TRAINING_PIPELINE_NAME_KEY = "pipeline_name"

# Data ingestion related variable

DATA_INGESTION_CONFIG_KEY = "data_ingestion_config"
DATA_INGESTION_ARTIFACT_DIR = "data ingestion"
DATA_INGESTION__DOWNLOAD_URL_KEY = "dataset download_url"
DATA_INGESTION__RAW_DATA_DIR_KEY = "raw data dir"
DATA_INGESTION__TGZ_DOWNLOAD_DIR_KEY = "tgz_download_dir"
DATA_INGESTION__DIR_NAME_KEY = "ingested_dir"
DATA_INGESTION_TRAIN_DIR_KEY = "ingested_train_dir"
DATA_INGESTION__TEST_DIR_KEY = "ingested_train_dir"