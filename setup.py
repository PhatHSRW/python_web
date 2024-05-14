from setuptools import setup, find_packages

setup(
    include_package_data=True,
    name="website",
    version="0.0.1",
    packages=find_packages(where="website")
)