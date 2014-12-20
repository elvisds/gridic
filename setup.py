#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    'mingus',
    'bottle'
]

test_requirements = [
    'mingus',
    'bottle'
]

setup(
    name='gridic',
    version='0.1.0',
    description='A grid-like interface to creating simple music',
    long_description=readme + '\n\n' + history,
    author='Elvis D\'Souza',
    author_email='me@elvis.co.in',
    url='https://github.com/elvisds/gridic',
    packages=[
        'gridic',
    ],
    package_dir={'gridic':
                 'gridic'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='gridic',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
