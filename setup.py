from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="AI travel assistant",
    version="0.2",
    author="Fatir",
    packages=find_packages(),
    install_requires = requirements,
)