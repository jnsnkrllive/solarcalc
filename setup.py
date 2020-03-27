import setuptools

from distutils.core import setup


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="solarcalc",
    version="0.1",
    description="Python Library for calculating solar positions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jnsnkrllive/solarcalc",
    author="Karl Jansen",
    author_email="jnsnkrl@live.com",
    license="MIT",
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Astronomy",
        "Topic :: Software Development :: Libraries"
    ]
)
