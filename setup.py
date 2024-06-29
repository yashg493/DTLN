import os
import platform

import pkg_resources
from setuptools import find_packages, setup


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="dtln",
    packages=["dtln"], 
    version="1.0.0",
    description="Dual-signal Transformation LSTM Network",
    readme="README.md",
    python_requires=">=3.8",
    author="YASH",
    url="https://github.com/yashg493/DTLN",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ],
    entry_points={
        "console_scripts": ["dtln=dtln.run_evaluation:cli"],
    },
    include_package_data=True,
)