from setuptools import find_packages, setup

setup(
    name='{{ cookiecutter.package_name }}',
    version='0.0.1',
    package_dir={"": "src"},
    packages=find_packages("src"),
    description='{{ cookiecutter.description }}',
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    keywords=[],
    author='{{ cookiecutter.author_name }}',
    license='{% if cookiecutter.open_source_license == 'MIT' %}MIT{% elif cookiecutter.open_source_license == 'BSD-3-Clause' %}BSD-3{% endif %}',
)
