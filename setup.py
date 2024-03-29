import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="twc-director",
    version="0.0.2",
    author="Garth Berry",
    author_email="garth@wiredsquare.com",
    description="Tesla Wall Charger Communication Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wired-square/twc-director",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[
        "aioserial",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
