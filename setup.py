from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:

    requirements_list:list=[str]
    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()

            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirements_list.append(requirement)
    except FileNotFoundError:
        print('requirement.txt file not found')
    return requirements_list
print(get_requirements())

setup(
    name="Network Security",
    version='0.0.1',
    author="Kenaz Jose",
    author_email="kenazjose007@gmail.com",
    packages=find_packages(),
    install_requirements=get_requirements()
)