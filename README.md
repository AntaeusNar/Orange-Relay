# Orange-Relay
Build a relay control system in Python, with a Django web interface on a OrangePi

Installing [Armbian](https://docs.armbian.com/) via [a little tutorial](https://lucsmall.com/2017/01/19/beginners-guide-to-the-orange-pi-zero/) for the base os.

Using the [OPi.GPIO](https://opi-gpio.readthedocs.io/en/latest/) python library although [pyA20](https://pypi.org/project/pyA20/) might be another option.

## Setup the PyCharm environment

### Windows:

1. Install [Python](https://www.python.org/downloads/)
   - Make sure to install pip and PATH as part of the installation of python
2. ```pip install --user virtualenv```
   - This will install [virtualenv](https://virtualenv.pypa.io/en/latest/)
3. ```python -m venv OR_env```
   - This will create the virtual environment
4. ```OR_env\Scripts\activate```
   - This will activate the virtual environment
5. ```pip install OPi.GPIO```
   - This will install the [OPi.GPIO](https://opi-gpio.readthedocs.io/en/latest/) library
6. ```pip install Django```
   - Installs [Django](https://www.djangoproject.com/) framework
8. Setup the Django project
   - ```django-admin startproject OR_web . ```
      - Starts the project
   - Add below to to _settings.py_ under INSTALLED_APPS
   ```python
   # My Apps
   'OR_web_GUI',
    ```
9. Setup the Django database (default is sqlite)
   - Run in terminal ```python manage.py migrate```
   - **NOTE: Any changes to models in _models.py_ will change the way the database works.  Please use the following instructions after every change:**
     - In the terminal ```python manage.py makemigrations OR_web_GUI```
     - In the terminal ```python manage.py migrate```
10. ```python manage.py startapp OR_web_GUI```
10. Start the Django server with ```python manage.py runserver```

## Git Workflow/Branch control:

Following some of the framework laid out in [Vincent Driessen's Article](https://nvie.com/posts/a-successful-git-branching-model/) this repo will use master as full release and autodeployment ready code, with development being the primary working/nightly build branch.  Hotfixes, bugfixes and new feature dev should each occur on their own branch then merged without fastforward into development or in the case of hotfixes, master. 
![](https://nvie.com/img/git-model@2x.png "Article Example")

## Release names:

For simplicity and ease of use each release will be version numbered and then titled after [The Muppets](http://muppet.wikia.com/wiki/Sesame_Street_character_debuts)