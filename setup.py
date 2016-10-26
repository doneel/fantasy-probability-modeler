# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='ffl_predictor',
    version='0.0.1',
    description='Predictive modeling for fantasy football leagues',
    long_description=readme,
    author='Daniel O\'Neel, Reed Johnson, Richard Tai',
    author_email='danieloneel@gmail.com',
    url='https://github.com/doneel/ffl_predictor',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')))
