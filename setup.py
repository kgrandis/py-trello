#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='py-trello',
    version='',
    author='Richard Kolkovich',
    author_email='richard@sigil.org',
    packages=find_packages(),
    include_package_data=True,
    install_requires = [
        'httplib2',
        'oauth2',
        ],
    test_suite = 'test.test_trello',
    url='https://github.com/sarumont/py-trello',
    description='Python client for Trello API',
    long_description=open('README.md').read(),
)
