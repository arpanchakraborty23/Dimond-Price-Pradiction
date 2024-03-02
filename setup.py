from setuptools import find_packages,setup
from typing import List
HYPEN_E='-e .'

def get_requierments(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''

    requirements=[]
    with open(file_path) as file_obj :        # open file itrate libaries
            requirements=file_obj.readlines()  # read every line reqirements.txt
            requirements=[req.replace('\n','') for req in requirements] # every itration /n will be add for remove that we use replace
           
            # ignore -e
            if HYPEN_E in requirements:
                requirements.remove(HYPEN_E)
    return requirements


setup(
    name='Diamond_predectionProject',
    version='0.0.1',
    author='Arpan',
    author_email='arpanchakraborty500@gmail.com',
    packages=find_packages(),
    instal_requires=get_requierments('requirements.txt')
)