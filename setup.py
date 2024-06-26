from setuptools import find_packages,setup # type: ignore
from typing import List 

"""HYPHEN_E_DOT='-e .'

def get_requirements(filepath:str)->List[str]:
    requirements=[]
    with open(filepath) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("/n","") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
            return requirements"""

setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='Darshan BR',
    author_email='darshanbr081@gmail.com',
    install_requires=["scikit-learn","pandas","numpy"],
    packages=find_packages()
)
     