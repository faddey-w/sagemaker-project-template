#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='sagemaker-poc',
    version='0.1.0',
    packages=find_packages(include=["my_project"]),
    install_requires=[
        'boto3==1.14.48',
    ],
)
