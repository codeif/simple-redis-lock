#!/usr/bin/env python
from setuptools import find_packages, setup

with open('README.rst') as f:
    readme = f.read()


setup(
    name='simple-redis-lock',
    version='0.1.0',
    description='A simple redis lock.',
    long_description=readme,
    author='codeif',
    author_email='me@codeif.com',
    url='https://github.com/codeif/simple-redis-lock',
    license='MIT',
    packages=find_packages(),
)
