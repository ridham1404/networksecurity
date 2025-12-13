'''
The setup.py file is an essential part of packaging and distributing Python projects. 
it is used bt setuptools to define the configuration of projects, such as  metadata 
and dependencies.
'''

from setuptools import setup, find_packages
from typing import List



def get_requirements()->List[str]: # this function will return the list of requirements
     requirements_lst:List[str]=[]
     try:
          with open("requirements.txt","r") as file:
               # Read all lines from the file
               lines=file.readlines()
               # Process each line to extract requirements
               for line in lines:
                    requirement=line.strip()
                    # ignore empty lines and -e .
                    if requirement and requirement!="-e .":
                         requirements_lst.append(requirement)
     except FileNotFoundError:
          print("requirements.txt file not found. No dependencies will be installed.")

     return requirements_lst

setup(
     name="NetworkSecurity",
     version="0.0.1",
     author="Ridham Prajapati",
     author_email="pridham42@gmail.com",
     packages=find_packages(),
     install_requires=get_requirements(),
     description="A project for network security",
)