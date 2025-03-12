from setuptools import setup, find_packages

setup(
    name="TMC2209_PY",  
    version="0.1.0",  
    author="Bashar Almadani",
    author_email="basharalmadani88@gmail.com",
    description="A Python library for controlling the TMC2209 stepper motor driver",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/bash227/TMC2209_Python", 
    license="MIT",
    packages=find_packages(include=["TMC2209_PY", "TMC2209_PY.*"]),
    install_requires=["pyserial"], 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
    
