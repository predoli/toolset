# setup.py
from setuptools import setup

setup(
    name="vb2homebank csv converter",
    version="0.1",
    author="Oliver Maier",
    author_email="olivermaier0@gmail.com",
    description="A csv data model converter from the volksbank export to a homebank readable format",
    license = "BSD",
    keywords = "csv converter volksbank homebank",
    url = "https://github.com/predoli/toolset/tree/master/vb2homebank",
    packages=['vb2homebanklib'],
    scripts=['vb2homebank']
)
