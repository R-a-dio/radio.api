#!/usr/bin/env python
from setuptools import setup


setup(
    name="radio.api",
    version="0.1.0",
    license="BSD",
    description="API to R/a/dio database, also includes a REST API.",
    author="Wesley Bitter",
    author_email="radio@wessie.info",
    url="http://github.com/R-a-dio/radio.api",
    namespace_packages=["radio"],
    install_requires=[
        "peewee",
        "flask-peewee",
    ],
    packages=["radio.api", "radio.api.rest"],
    tests_require=["pytest"],
)
