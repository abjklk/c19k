import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="C19 Karnataka Stats",
    version="0.0.1",
    author="abjklk",
    author_email="abjklk@gmail.com",
    description="C19 Data Tracker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abjklk/c19k",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)