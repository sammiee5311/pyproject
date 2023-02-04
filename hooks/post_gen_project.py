import os
import shutil


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


if "{{ cookiecutter.open_source_license }}" == "Not open source":
    remove(os.path.join(os.getcwd(), "{{ cookiecutter.project_slug }}", "LICENSE"))

if "{{ cookiecutter.github_actions }}" == "n":
    remove(os.path.join(os.getcwd(), "{{ cookiecutter.project_slug }}", ".github"))

if "{{ cookiecutter.github_actions }}" == "n":
    remove(os.path.join(os.getcwd(), "{{ cookiecutter.project_slug }}", "tox.ini"))


print("Generated files from cookiecutter.")
