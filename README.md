# klagomuren

## Setup
To install modules, you need the python package manager pip (sudo apt-get install pip). In this project, we have used the Python IDE Pycharm, but use on of your liking. To create the correct folder structure, run the file 'init_project.py'
Virtual environments

It is recommended to use a virtual environment to install packages in, so they don't get installed globally. There are many tools for this but the most used low-lever is called virtualenv.

    pip install virtualenv

Create a virtual environment for a project:

    cd my_project_folder virtualenv my_project

This creates a copy of Python in whichever directory you ran the command in, placing it in a folder named 'my_project'. To begin using the virtual environment, it needs to be activated:

    source my_project/bin/activate

This will now show in the terminal prompt. To deactivate the venv, just use the command

    deactivate

In Pycharm, you can also choose the virtualenv to be the standard python interpreter.
