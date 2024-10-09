from os import path
from setuptools import find_packages, setup

if path.exists('README.md'):
    with open('README.md') as readme:
        long_description = readme.read()



setup(
    name="bayes24",
    version='0.0.dev0',
    description="Course materials for Bayesian Statistics for Astrophysics 2024",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/t-kist/Bayesian-Statistics-for-Astrophysics-2024",
    author='Timo Kist',
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "numpy",
        "scipy",
        "matplotlib",
        "ipython",
        "jupyter"],
    dependency_links=[],
    scripts=[],
)
