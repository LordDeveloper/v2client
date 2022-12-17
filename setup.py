import setuptools
from os import path

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open('README.md') as f:
    long_description = f.read()
    
try:
    with open(path.join(here, "requirements.txt"), encoding="utf-8") as r:
        requirements = [i.strip() for i in r]
except FileNotFoundError:
    requirements = ['grpcio==1.49.1', 'grpcio-tools==1.38.1', 'protobuf==3.20.3']
try:
    with open(path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = 'https://github.com/LordDeveloper/v2client/README.md'

setuptools.setup(
    name="v2client",
    version="1.1.0",
    author="Mostafa Mosavi",
    author_email="mostafa.uwsgi@gmail.com",
    description="A V2Ray/V2Fly client for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/its0x4d/v2client",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license='MIT',
    python_requires='>=3.6',
)
