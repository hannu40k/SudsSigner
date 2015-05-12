#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Basic setup script. Still no dependecy information


# python-libxml2 / libxml2-python should be installed before
# because it does not install from PyPi.
# It's part of libxml2 and may be present as separate package
# e.g. python-libxml2 on Ubuntu, libxml2-python on RHEL/CentOS
# All other dependencies should work.
# Tested with virtualenv --distribute and python 2.7 on Ubuntu 12.04
# after copying libxml2 manually from system folder.
from setuptools import setup
import sudssigner

setup(
    name='sudssigner',
    version=sudssigner.__version__,
    packages=['sudssigner'],
    install_requires=[
        'lxml', 'pyopenssl', 'suds-jurko>=0.6',
        'pyxmlsec'],
    author=u'András Veres-Szentkirályi',
    author_email='vsza@vsza.hu',
    maintainer='Ernesto Revilla',
    maintainer_email='erevilla@tangrambpm.es',
    description='Sign digitally suds WS requests with X509v3 certificates',
    license='MIT license',
    url='https://github.com/dnet/SudsSigner',
    plataforms=['Linux', 'Windows', 'OSX'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development :: SOAP WS Client',
        ],
)
