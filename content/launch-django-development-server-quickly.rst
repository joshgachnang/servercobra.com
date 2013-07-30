Launch Django Development Server Quickly
########################################
:date: 2010-11-30 11:55
:author: Josh
:category: Articles
:tags: Django
:slug: launch-django-development-server-quickly

I hate repetitive anything, so you can understand my frustration typing
the following to start the Django development server:

.. code-block:: bash

	cd PROJECT\_DIRECTORY
	python manage.py runserver



So I decided to make a quick BASH alias, so I only type 4 characters per
project.  Assuming you're using Ubuntu, let's edit our BASH config file:

.. code-block:: bash

	nano ~/.bashrc
	#At the bottom of the file, add this line, replacing it with the path to your project directory
	alias djan:'python ~/programming/project/manage.py runserver'



A few quick tips I've found to be handy:

#. Do one per Django project, so you can quickly open a terminal, type 4
   characters, and have the dev server up.
#. You can do this for any of the manage.py commands (syncdb, etc)
#. You can also do another alias for just the runserver command, not
   specific to any project like this:

.. code-block:: bash

	alias dj='python manage.py runserver'



Of course, that requires you to be in the directory of the Django
project, but I spend a lot of my terminal time there, so this makes
sense. Here's an example of it running:

.. code-block:: bash

	josh@josh-desktop:~$ mlio
	Validating models...
	0 errors found

| Django version 1.2.3, using settings 'MyLifeIsOpen.settings'
	Development server is running at http://127.0.0.1:8000/
	Quit the server with CONTROL-C.



Easy, right?

If you use any awesome time savers like this in Django, please post them
in the comments so we can all save time!
