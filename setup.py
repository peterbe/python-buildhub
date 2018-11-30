import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="python-buildhub",
    version="0.0.1",
    description="Python interface to Buildhub service",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/peterbe/python-buildhub",
    author="Peter Bengtsson",
    author_email="mail@peterbe.com",
    license="MPL2",
    classifiers=[
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["buildhub"],
    include_package_data=True,
    install_requires=["requests"],
    extras_require={
        "dev": ["twine", "therapist", "black", "flake8", "bumpversion", "tox"]
    },
    # entry_points={
    #     "console_scripts": [
    #         "buildhub=buildhub.__main__:main",
    #     ]
    # },
)
