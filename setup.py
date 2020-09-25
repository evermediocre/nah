from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="nah",
    version="0.1.0",
    description="A collection of simple error handling function decorators",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/onchie/nah",
    author="Onchie Cantillo",
    author_email="eihcno@gmail.com",
    py_modules=["nah"],
    package_dir={"": "src"},
    tests_require=["pytest"],
    test_suite="tests",
    python_requires=">=3.5",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    extras_require={
        "dev": [
            "pytest~=6.0.2"
        ]
    }
)
