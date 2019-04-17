#!/usr/bin/env python
from setuptools import setup, find_packages
from glob import glob
from distutils.core import setup, Command
import distutils.command.install 
import os.path

# Set __version__
exec(open('snakePipes/__init__.py').read())

scripts = ['bin/snakePipes']
for d in glob('snakePipes/workflows/*'):
    scripts.append(os.path.join(d, os.path.split(d)[1]))


class InstallCommand(Command):
    description = "Installs the foo."
    user_options = [
        ('mpi-organisms', None, 'Insall the organism files.'),
    ]
    def initialize_options(self):
        self.foo = None
    def finalize_options(self):
        assert self.foo in (None, 'myFoo', 'myFoo2'), 'Invalid foo!'
    def run(self):
        print("test")

class BuildPyCommand(distutils.command.install.install):
    user_options = distutils.command.install.install.user_options + [
        ('foo=', None, 'Insall the organism files.'),
    ]
    def initialize_options(self):
        self.foo = None
    def finalize_options(self):
        assert self.foo in (None, 'myFoo', 'myFoo2'), 'Invalid foo!'
    def run(self):
        distutils.command.install.install.run(self)
        print("test")

setup(
    name='snakePipes',
    version=__version__,  # noqa: F821
    scripts=scripts,
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/maxplanck-ie/snakepipes',
    license='GPL v3',
    description='Snakemake workflows and wrappers for NGS data processing from the MPI-IE',
    zip_safe=False,
    cmdclass={
        'install': BuildPyCommand
    }
)
