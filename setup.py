from setuptools import setup, find_packages


with open("README.md", 'r') as fh:
    long_description = fh.read()

setup(
    name="ads",
    version="0.0.1",
    author="Alec Schneider",
    author_email="alecschneid@gmail.com",
    description="Small package for my won personal data analysis",
    long_description=long_description,
    url="https://github.com/Alec-Schneider/ads",
    packages=find_packages(),
    # classifiers=[
    #     "Programming Language :: Python :: 3",
    # ],
    python_requires='>=3.0'
)