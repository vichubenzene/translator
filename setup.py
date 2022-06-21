import setuptools

with open("README.md", "r", encoding ="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "benzene_translator",
    version = "0.2.1",
    author = "viswanathan s",
    author_email = "vichusathappan@gmail.com",
    description = "Translator",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/vichubenzene/translator",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6"
)
