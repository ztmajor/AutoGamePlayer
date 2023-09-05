#!/usr/bin/env python
from setuptools import setup, find_packages
from os import path
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='autogameplayer',
    version='0.0.0',
    description='autogameplayer',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Mei Yu',
    author_email='bzm8462@126.com',
    packages=find_packages(),
    python_requires=">=3.5",
    install_requires=[
        "pyautogui",
        "configargparse"
    ],
    entry_points={
        "console_scripts": [
            "start=autogameplayer.bin.start:main", 
        ],
    },
    platforms='any',
)
