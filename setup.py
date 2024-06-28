import os
import platform

import pkg_resources
from setuptools import find_packages, setup

setup(
    name="dtln",
    py_modules=["dtln"],
    version="1.0.0",
    description="Dual-signal Transformation LSTM Network",
    readme="README.md",
    python_requires=">=3.8",
    author="YASH",
    url="https://github.com/yashg493/DTLN",
    license="MIT",
    package_dir={'': 'src'},
    packages=find_packages(where="src", exclude=["tests*"]),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ],
    entry_points={
        "console_scripts": ["dtln=src.dtln.run_evaluation:cli"],
    },
    include_package_data=True,
    extras_require={"dev": ["pytest"]},
)