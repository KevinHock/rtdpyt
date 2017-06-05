Virtual env setup guide
=======================

Create a directory to hold the virtual env and project

``mkdir ~/a_folder``

``cd ~/a_folder``

Clone the project into the directory

``git clone https://github.com/python-security/pyt.git``

Create the virtual environment

``python3 -m venv ~/a_folder/``

Check that you have the right versions

``python --version`` sample output ``Python 3.6.0``

``pip --version`` sample output ``pip 9.0.1 from /Users/kevinhock/a_folder/lib/python3.6/site-packages (python 3.6)``

Change to project directory

``cd pyt``

Install dependencies

``pip install -r requirements.txt``

``pip list`` sample output ::

    gitdb (0.6.4)
    GitPython (2.0.8)
    graphviz (0.4.10)
    pip (9.0.1)
    requests (2.10.0)
    setuptools (28.8.0)
    smmap (0.9.0)

In the future, just type ``source ~/a_folder/bin/activate`` to start developing.