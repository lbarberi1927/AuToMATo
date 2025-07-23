from setuptools import setup, find_packages

setup(
    name="AuToMATo",
    version="0.1.0",
    packages=find_packages(include=["automato*", "bottleneck_bootstrap*", "persistence_plotting*"]),
    install_requires=[],
)
