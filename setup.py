from setuptools import setup, find_packages

setup(
    name="folderflow",
    version="1.0",
    author="Your Name",
    description="A CLI tool to organize files by type.",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "folderflow=folderflow.cli:main"
        ]
    },
    python_requires='>=3.6',
)
