#!/usr/bin/env python
from setuptools import setup, find_packages
from setuptools.command.install import install
from glob import glob
import sys
#from distutils.core import setup, Command
#import distutils.command.install 
import os.path

# Set __version__
exec(open('snakePipes/__init__.py').read())

scripts = ['bin/snakePipes']
for d in glob('snakePipes/workflows/*'):
    scripts.append(os.path.join(d, os.path.split(d)[1]))

addData = {}

if "--addOrganismFiles" in sys.argv:
    addData = {'snakePipes': ['shared/organisms/*.yaml']}
    sys.argv.remove("--addOrganismFiles")

# class BuildPyCommand(install):
#     addData
#     user_options = install.user_options + [
#         ('addOrganismFiles', None, 'Install the organism files.'),
#     ]
#     def initialize_options(self):
#         install.initialize_options(self)   
#         self.addOrganismFiles = None
#     def finalize_options(self):
#         print(self.addOrganismFiles)
#         install.finalize_options(self)
#         if self.addOrganismFiles==1:
#             self.addData = {'snakePipes': ['shared/organisms/*.yaml']}
#     def run(self):
#         install.run(self)
#         #print(self.addOrganismFiles)
#         if self.addOrganismFiles==1:
#             self.addData = {'snakePipes': ['shared/organisms/*.yaml']}
#         print(self.addData)

setup(
   # cmdclass={
   #     'install': BuildPyCommand
   # },
    name='snakePipes',
    version=__version__,  # noqa: F821
    scripts=scripts,
    packages=find_packages(),
    include_package_data=True,
    package_data=addData,
    url='https://github.com/maxplanck-ie/snakepipes',
    license='GPL v3',
    description='Snakemake workflows and wrappers for NGS data processing from the MPI-IE',
    zip_safe=False,
)
