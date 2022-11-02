from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="consulta_clima",
    version="0.0.1",
    author="Cleison Silva",
    author_email="cleisoninfo2013@gmail.com",
    description="Package to consult the current climate of a city",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cleison0silva/pacote_api_clima.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)