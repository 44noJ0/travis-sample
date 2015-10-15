import os
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

requires = []

setup(
    name='mod',
    version='1.0.0',
    description='Mod is awesome module for Python',
    long_description='module',
    classifiers=[
        "Programming Language :: Python",
    ],
    author='Takahiro Yoshimura',
    author_email='altakey@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    install_requires = requires
)
