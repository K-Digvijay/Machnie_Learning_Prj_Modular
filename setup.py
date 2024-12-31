from setuptools import setup, find_packages
from typing import List

PROJECT_NAME = 'Machine_Learning'
VERSION = '0.0.1'
DESCRIPTION = 'This is my first moduler ML Project'
AUTHOR_NAME = 'Digvijay'
EMAIL_ID = 'digvijay.kewale@gmail.com'

REQUIRMENT_FILE_NAME = 'requirments.txt'
HYPHEN_E_DOT = '-e .'

def Get_requirment_list() -> list[str]:
    with open(REQUIRMENT_FILE_NAME) as requirment_file:
        requirment_list = requirment_file.readline()
        requirment_list = [requirment_name.replace('\n',"") for requirment_name in requirment_list]

        if HYPHEN_E_DOT in requirment_list:
            requirment_list.remove(HYPHEN_E_DOT)

        return requirment_list


setup(
    name=PROJECT_NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR_NAME,
    author_email=EMAIL_ID,
    packages=find_packages(),
    install_requires = Get_requirment_list()
)





