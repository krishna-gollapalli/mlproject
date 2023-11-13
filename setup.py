from setuptools import find_packages, setup

HYPEN_E_DOT='-e .'


def get_requirements(file_path:str)->[str]:
    '''
    this function will load file path and returns the list of values in the file as requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Krishna G',
author_email='gollapalli.k@northeastern.edu',
packages=find_packages(),
install_requires= get_requirements('requirements.txt')

)

