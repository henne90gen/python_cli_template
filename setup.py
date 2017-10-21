import os
from setuptools import setup


def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


setup(
    name="cli_template",
    version="0.0.1",
    author="Name",
    author_email="",
    packages=['cli_template', 'tests'],
    install_requires=['cement'],
    long_description=read('README.md'),
    description="Command line application",
)
