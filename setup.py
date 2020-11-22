from setuptools import find_packages, setup

with open('README.md') as f:
    readme = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    install_requires=requirements,
    packages=find_packages(exclude=('tests', 'cfg'))
)
