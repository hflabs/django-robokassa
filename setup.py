#!/usr/bin/env python
#coding: utf-8
from distutils.core import setup

for cmd in ('egg_info', 'develop'):
    import sys
    if cmd in sys.argv:
        from setuptools import setup

import sys
reload(sys).setdefaultencoding("UTF-8")

setup(
    name='django-robokassa-modern',
    version='1.3',
    author='Mikhail Korobov',
    author_email='kmike84@gmail.com',
    
    maintainer = "alrusdi",
    maintainer_email = "alrusdi@gmail.com",

    packages=['robokassa', 'robokassa.migrations'],

    url='https://github.com/hflabs/django-robokassa',
    license = 'MIT license',
    description = u'Приложение для интеграции платежной системы ROBOKASSA в проекты на Django.'.encode('utf8'),
    long_description = open('README.rst').read().decode('utf8') + u"\n\n" + open('CHANGES.rst').read().decode('utf8'),

    requires=['django (>= 1.7)'],

    classifiers=(
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: Russian',
    ),
)
