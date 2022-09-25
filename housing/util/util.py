from cmath import e
from readline import read_init_file
import yaml
from housing.exception import HousingException
import os,sys
import numpy as np
import dill

def read_yaml_file(file_path:str)->dict:
    """
    Reads a YAML file and returns the contains as a dictionary.
    file_path: str
    """
    try:
        with open(file_path,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException(e,sys) from e
def save_numpy_array_data(file_path:str,array:np.array):
    """
    save numpy array data to file
    file path: str location of file to save
    array: np.array data to save 
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,'wb') as file_obj:
            np.save(file_obj,array)
    except Exception as e:
        raise HousingException(e,sys) from e


def load_numpy_array_data(file_path:str) ->np.array:
    """
    load numpy arrray data from file
    file path : str location of file load
    return: np.array data loaded
    """
    try:
        with open(file_path,'rb') as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise HousingException(e,sys) from e

def save_object(file_path:str,obj):
    """
    file path :str
    obj: Any sort of object
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        raise HousingException(e,sys) from e

def load_object(file_path:str):
    """
    file_path:str
    """
    try:
        with open(file_path,'rb') as file_obj:
            return dill.load(file_obj)

    except Exception as e:
        raise HousingException(e,sys) from e