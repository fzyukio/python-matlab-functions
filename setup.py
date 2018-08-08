import setuptools
from codecs import open


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pymlfunc",
    version="0.0.2",
    author="Yukio Fukuzawa",
    author_email="y.fukuzawa@massey.ac.nz",
    description="Implementation of some useful Matlab functions that are missing from numpy/scipy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fzyukio/python-matlab-functions",
    packages=setuptools.find_packages(),
    install_requires=['numpy', 'scipy'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)