from setuptools import find_packages, setup

dev_requires = [
    "pytest",
    {% if cookiecutter.black|lower == 'y' -%}
    "black",
    {% endif -%}
    {%- if cookiecutter.mypy|lower == 'y' -%}
    "mypy",
    {% endif -%}
    {%- if cookiecutter.isort|lower == 'y' -%}
    "isort",
    {% endif -%}
]

if __name__ == "__main__":
    setup(
        name="{{ cookiecutter.project_name }}",
        author="{{ cookiecutter.author_name }}",
        author_email="{{ cookiecutter.email }}",
        description="{{ cookiecutter.project_description }}",
        packages=find_packages(exclude=("tests")),
        install_requires=[],
        extras_require={"dev": dev_requires},
    )