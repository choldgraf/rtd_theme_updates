#!/usr/bin/env python

import codecs
from setuptools import setup

# Version info -- read without importing
_locals = {}
with open("sphinx_rtd_jupyter/_version.py") as fp:
    exec(fp.read(), None, _locals)
version = _locals["__version__"]

setup(
    name="sphinx_rtd_jupyter",
    version=version,
    description="A configurable sidebar-enabled Sphinx theme for Project Jupyter",
    author="Project Jupyter",
    author_email="jupyter@googlegroups.org",
    url="https://github.com/jupyterhub/sphinx-rtd-jupyter",
    packages=["sphinx_rtd_jupyter"],
    include_package_data=True,
    entry_points={"sphinx.html_themes": ["sphinx_rtd_jupyter = sphinx_rtd_jupyter"]},
    install_requires=[
       'sphinx',
       'sphinx_rtd_theme',
    ]
)
