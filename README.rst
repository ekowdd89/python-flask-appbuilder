Base Skeleton to start your application using Flask-AppBuilder
--------------------------------------------------------------

- Install it::

	pip install flask-appbuilder
	git clone https://github.com/ekowdd89/python-flask-appbuilder.git

- VirtualEnv::

    $ virtualenv flask_app_venv
    $ source ./flask_app_venv/bin/activate

- Run it::

    $ export FLASK_APP=app
    # Create an admin user
    $ flask fab create-admin
    # Run dev server
    $ flask run


That's it!!
