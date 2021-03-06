from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="sequence_fibonacci",
    version="0.0.1",
    author="Carlos Alberto Silva Júnior",
    author_email="casjunior93@gmail.com",
    description="Returns a sequence of n Fibonacci numbers.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/casjunior93/pacote-python-para-gerar-n-numeros-da--sequencia-fibonacci"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
