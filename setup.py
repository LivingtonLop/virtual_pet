from setuptools import setup, find_packages
import os

def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(
    name='virtual_pet',
    version='1.0',
    packages=find_packages(),
    author='lllc',
    description='Practica 02',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    entry_points={
        'console_scripts': [
            'virtual_pet_execute=src.main:main',
        ],
    },
)
