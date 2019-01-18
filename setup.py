import io
from setuptools import setup

with io.open("requirements.txt") as f:
    install_requires = f.read().splitlines()

with io.open("test-requirements.txt") as f:
    tests_require = f.read().splitlines()

with io.open("README.rst") as f:
    long_description = f.read()

setup(
    name="aiohttp-limit",
    version="0.1.0",
    url="https://github.com/underyx/aiohttp-limit",
    author="Bence Nagy",
    author_email="bence@underyx.me",
    maintainer="Bence Nagy",
    maintainer_email="bence@underyx.me",
    download_url="https://github.com/underyx/aiohttp-limit/releases",
    description="An aiohttp middleware for limiting connections",
    long_description=long_description,
    packages=["aiohttp_limit"],
    tests_require=tests_require,
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
    ],
)
