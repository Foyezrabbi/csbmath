
from setuptools import setup, find_packages
from os import path
import csbmath


long_description = """
**csbmath - Search emails through Search Engines**
======================================================

Installation:
-------------

    > pip3 install csbmath

Upgrades are also available using:

    > pip3 install csbmath --upgrade

Search Engines
--------------

- google: Ok (note cookies policy and Captcha!).
- bing: OK.
- baidu: OK (few requests).
- bing: Hunting Robots very fast.

Usage
-----

EmailFinder can be used in 2 ways:

CLI
---

    csbmath -d domain.com

Parameters: 

- d: Specifies the target domain.
- v: Show EmailFinder version.
- p: HTTP proxy server URL.


In Code
-------

from csbmath.extractor import *


emails1 = get_emails_from_google("domain.com")
emails2 = get_emails_from_bing("domain.com")
emails3 = get_emails_from_baidu("domain.com")


Author
======

This project has been developed by:

-  **Josué Encinar García** -- https://twitter.com/JosueEncinar


Disclaimer!
===========

The software is designed to check a company's emails found in the search engines. The author is not responsible for any
illegitimate use.



"""

setup(
    name='CSB-Math',
    version=csbmath.__version__,
    author='Foyez Rabbi (@Foyez_Rabbi)',
    description='CSB-Math - math search through Search Engines',
    include_package_data=True,
    license='apache',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/foyezrabbi/csbmath",
    entry_points={
        'console_scripts': [
            'csbmath=csbmath.cli:main',
        ],
    },
    install_requires=[
        "requests>=2.25.1",
        "prompt-toolkit>=3.0.5",
        "urllib3>=1.26.4",
        "pyfiglet>=0.8.post1",
        "beautifulsoup4>=4.9.3"
    ]
)
