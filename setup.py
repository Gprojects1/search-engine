from setuptools import setup

setup(
    name="count_pairs",
    version="1.0",
    packages=["count_pairs"],
    install_requires=["behave"],
    entry_points={
        "console_scripts": ["count_pairs_cli=count_pairs.main:main"],
    },
)