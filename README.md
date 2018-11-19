# Orange-Relay
Build a relay control system in Python, with a Django web interface on a OrangePi

Installing [Armbian](https://docs.armbian.com/) via [a little tutorial](https://lucsmall.com/2017/01/19/beginners-guide-to-the-orange-pi-zero/) for the base os.

Using the [OrangePi.GPIO](https://github.com/Jeremie-C/OrangePi.GPIO) python library although [pyA20](https://pypi.org/project/pyA20/) might be another option.

## Setup the PyCharm environment

###Windows:

1. Install [Python](https://www.python.org/downloads/)
   - Make sure to install pip and PATH as part of the installation of python
2. ```pip install --user virtualenv```
   - This will install [virtualenv](https://virtualenv.pypa.io/en/latest/)
3. ```python -m venv OR_env```
   - This will create the virtual environment
4. ```OR_env\Scripts\activate```
   - This will activate the virtual environment
5. ```pip install OrangePi.GPIO```
   - This will install the [OrangePi.GPIO](https://github.com/Jeremie-C/OrangePi.GPIO) library
6. ```pip install Django```
   - Installs [Django](https://www.djangoproject.com/) framework
7. ```pip install django-bootstrap4```
   - Installs [Bootstrap 4](https://django-bootstrap4.readthedocs.io/en/latest/)
8. Setup the Django project
   - ```django-admin startproject OR_web . ```
      - Starts the project
   - Add below to to _settings.py_ under INSTALLED_APPS
   ```python
   # My Apps
   'OR_web',
   
   # Third Party Apps
   'bootstrap4',
   ``` 
   - Add below to _settings.py_ at end
   ```python
          # Settings for django-bootstrap4
          BOOTSTRAP4 = {
            'include_jquery' : True,
          }
   ```
9. Setup the Django database (default is sqlite)
   - Run in terminal ```python manage.py migrate```
   - **NOTE: Any changes to models in _models.py_ will change the way the database works.  Please use the following instructions after every change:**
     - In the terminal ```python manage.py makemigrations OR_web```
     - In the terminal ```python manage.py migrate```
10. Start the Django server with ```python manage.py runserver```