#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import farmguru
version = farmguru.__version__

setup(
    name='farmguru',
    version=version,
    author="Savio Abuga",
    author_email='savioabuga@gmail.com',
    packages=[
        'farmguru',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.4',
    ],
    zip_safe=False,
    scripts=['farmguru/manage.py'],
)
