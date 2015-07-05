July 2015 Django Class
======================

This repository was created to support the class Django class taught July 2015.

Installation
============

To begin you can clone this repository and setup Django using the following instructions.

Linux Installation (Debian/Ubuntu)
----------------------------------

Note:

    - The following will assume you are cloning the sourcecode to **~/Projects/july-2015-django-class**.  If you are cloning to a different location, you will need to adjust these instructions accordingly.
    - A dollar sign ($) indicates a terminal prompt, as your user, not root.

1.  Clone the source::

        $ cd ~/Projects
        $ git clone git@github.com:ricomoss/july-2015-django-class.git

2. Install some required packages::

        $ sudo apt-get install python3 python3-dev python-pip

3.  Install virtualenv and virtualenvwrapper::

        $ pip install virtualenv
        $ pip install virtualenvwrapper

4.  Add the following to your **~/.bashrc** or **~/.zshrc** file::

        source /usr/local/bin/virtualenvwrapper.sh

5.  Type the following::

        $ source /usr/local/bin/virtualenvwrapper.sh

6.  Create your virtualenv (for Python 3)::

        $ mkvirtualenv jdc -p /usr/bin/python3


7.  Add the following to the end of the file **~/.virtualenvs/jdc/bin/postactivate**::

        export DJANGO_SETTINGS_MODULE=website.settings
        export PYTHONPATH=~/Projects/july-2015-django-class/<class_folder>

8.  Activate the virtualenv::

        $ workon jdc

9.  Install the required Python libraries (ensure you're within the new virtual environment).::

        (jdc)$ pip install -r ~/Projects/july-2015-django-class/requirements.pip

10.  Sync the database (follow the Django instructions).::

        (owf)$ python ~/Projects/july-2015-django-class/<class_folder>/manage.py syncdb
        
11.  Start the runserver.::

        (owf)$ python ~/Projects/july-2015-django-class/<class_folder>/manage.py runserver
        
12.  Open your browser and see your site.::

        http://127.0.0.1:8000/


OSX Installation
----------------------------------

Note:

        - The following will assume you are cloning the sourcecode to **~/Projects/july-2015-django-class**.  If you are cloning to a different location, you will need to adjust these instructions accordingly.
        - A dollar sign ($) indicates a terminal prompt, as your user, not root.

1.  Clone the source::

        $ cd ~/Projects
        $ git clone git@github.com:ricomoss/july-2015-django-class.git

2.  Install Xcode if you don't have it already.  You can find it in the Apple store.  Install the Command Line Tools of Xcode.::

        $ xcode-select --install

3.  Install Homebrew.::

        $ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
        
4.  Add Homebrew to your `PATH`.  Do this by modifying your `rc` file (`bashrc`, `zshrc`, etc).  You'll need to source this file before the changes will take effect.::

        export PATH=/usr/local/bin:$PATH
        
5.  Install Python 3.  This example will work with Python 2.7 - but Python 3 is cooler!::

        $ brew install python3
        
6.  Install virtualenvwrapper::

        $ pip3 install virtualenv
        $ pip3 install virtualenvwrapper

7.  Run `virtualenv-burrito` to help setup your virtual environment without the normal MAC issues.::

        $ curl -sL https://raw.githubusercontent.com/brainsik/virtualenv-burrito/master/virtualenv-burrito.sh | $SHELL

8.  Create your virtualenv (for Python 3)::

        $ mkvirtualenv owf -p /usr/local/bin/python3


7.  Add the following to the end of the file **~/.virtualenvs/jdc/bin/postactivate**::

        export DJANGO_SETTINGS_MODULE=website.settings.dev
        export PYTHONPATH=~/Projects/july-2015-django-class/<class_folder>

8.  Activate the virtualenv::

        $ workon jdc

9.  Install the required Python libraries (ensure you're within the new virtual environment).::

        (jdc)$ pip3 install -r ~/july-2015-django-class/requirements.pip

10.  Sync the database (follow the Django instructions).::

        (jdc)$ python ~/Projects/july-2015-django-class/<class_folder>/manage.py syncdb
        
11.  Start the runserver.::

        (jdc)$ python ~/Projects/july-2015-django-class/<class_folder/manage.py runserver
        
12.  Open your browser and see your site.::

        http://127.0.0.1:8000/
