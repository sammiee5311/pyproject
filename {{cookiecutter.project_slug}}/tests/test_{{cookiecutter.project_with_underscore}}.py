from utils.log import logger

def test_{{cookiecutter.project_with_underscore}}():
    assert True

def test_logger():
    assert "{{ cookiecutter.project_name }}" == logger.name
