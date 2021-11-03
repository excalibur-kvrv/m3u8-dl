from setuptools import setup, find_packages, Extension

DESCRIPTION = 'm3u8 playlist downloader'
VERSION = "0.1.1"


with open("README.md") as fh:
    LONG_DESCRIPTION = fh.read()

setup(
    name="m3u8dl",
    version=VERSION,
    zip_safe=False,
    author="Kevin Rohan Vaz",
    author_email="excalibur.krv@gmail.com",
    maintainer='Vaibhav Lodha',
    maintainer_email='vlodha98@gmail.com',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/excalibur-kvrv/m3u8-dl",
    packages=find_packages(),
    install_requires=[
        "hyper==0.7.0",
        "PyInstaller==3.6",
        "requests==2.24.0",
        "progress~=1.5"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
