#!/usr/bin/env python
from setuptools import setup

setup  (
    name        = 'snakevm',
    version     = '1.0.1',
    description = 'A simple virtual machine and program assembler',
    author = 'Travis Cunningham',
    author_email = 'travcunn@umail.iu.edu',
    url = 'https://github.com/travcunn/simple_cpu',
    license = 'MIT',
    packages  =  ['snake'],
    package_dir = {'snake': 'snake'},
    entry_points = {
        'console_scripts': [
            'snakevm = snake.cli:vm',
            'assembler = snake.cli:assembler',
            'compiler = snake.cli:compiler',
        ],
    },
    install_requires=[
        'pytest',
        'pytest-cov',
        'mock',
        'tox',
    ],
)
