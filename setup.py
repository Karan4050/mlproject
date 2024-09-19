from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT="-e ."
def get_requirements(file_path:str)->list[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readline()
        requirements = [req.replace("\n"," ") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

setup(
name = 'mlproject',
version = '0.0.1',
author = 'KARAN',
author_email = 'karanparmar9733@gmail.com',
packages = find_packages(),
install_require = get_requirements('requirements.txt'),

)