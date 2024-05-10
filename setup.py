from setuptools import setup, find_packages

setup(
    name="msuliot.utils",
    version="0.2.0",
    author="Michael Suliot",
    author_email="michael@suliot.com",
    description="Some basic helper functions for AI projects",
    long_description=open('README.md').read(),
    url="https://github.com/msuliot/package.utils.git",
    packages=find_packages(),
    install_requires=[
        
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',
)
