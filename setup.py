from setuptools import setup
from typing import List



# declearing variable for setup function
PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="ISHAWANT"
DESCRIPTION="This is my machine learning project"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement mention in requirements.txt file

    retrun this funciton is going to return a list which contain name of libraries mentioned in requirements.txt file 
    """
    
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_file.readlines()

setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
install_requires=get_requirements_list()
)

# check requirement code is working or not
# if __name__=="__main__":
#     print(get_requirements_list())