"""
setup.py is a build script for Python projects. It's used to define how a Python package should be built, 
distributed, and installed. When you're creating a Python library or application that others can install using pip, 
you typically include a setup.py file at the root of your project.

📦 Purpose of setup.py
It tells Python how to:

Package your project

Define metadata (name, version, author, etc.)

List dependencies

Specify which files to include

Provide entry points (like console scripts)

"""

from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This Function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[r.replace('\n','')for r in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name = "ML-Projects",
    version="0.0.1",
    author = "Ayushman Mishra",
    author_email="mishraayush290705@gmail.com",
    packages=find_packages(),
    install_requires =get_requirements('requirements.txt')

    

)










