from setuptools import setup, find_packages
from typing import List

DASH_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements = []
    
    with open(file_path) as file:
        requirements = [line.strip() for line in file if line.strip() != DASH_E_DOT ]
    
    return requirements

setup(
    name='ml_setup_tutorial_2',
    author='etietop abraham',
    description='Learn to setup your environment for ml projects',
    version='0.0.1',
    author_email='etietopdemasabraham@gmail.com',
    packages=find_packages(),
    install_requirements = get_requirements('requirements.txt')
)