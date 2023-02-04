# {{ cookiecutter.project_name }}

# Setup Environment
- Dev
    - Run `make setup-dev-{{ cookiecutter.project_slug }}`
- Prod
    - Run `make setup-{{ cookiecutter.project_slug }}`

# Test
- Pytest
    - Run `make test-ci-{{ cookiecutter.project_slug }}`
- Tox
    - To run tox, python versions in the default setting are `3.8`, `3.9`, and `3.10`. You can configure the python versions in `tox.ini` file.
    - Run `make test-{{ cookiecutter.project_slug }}`
