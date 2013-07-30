Django New Project Checklist
############################
:date: 2011-01-18 14:38
:author: Josh
:category: Articles
:tags: Django, Python
:slug: django-start-project-checklist

Every time I start a new Django project, I also have to go back
through other projects to find all the tweaks I make to customize Django
to my liking. Here are some basics, and I'm sure I'll be tweaking this
as I write more and more Django apps.


If you don't already have Django installed (assuming you're using
Debian/Ubuntu)

.. code-block:: bash

	sudo apt-get install python-django



Start a Django project:

.. code-block:: bash

	django-admin.py startproject example
	#On my Ubuntu 10.04 box, this works instead:
	#django-admin startproject example



Project naming note:
Django won't let you make names with dashes in them (only numbers,
letters, and underscores). So choose wisely! I generally do all lower
case and underscores.

Enter the project and make the first app:

.. code-block:: bash

	cd example/
	python manage.py startapp exampleapp



Create a useful .gitignore: (If using git that is)

.. code-block:: bash

	nano .gitignore
	------

    \*.pyc
	\*~



Get the settings and database ready:

.. code-block:: bash

	touch sqlite3.db
	nano settings.py
	------

    #Add this near the top
	import os
	dirname = os.path.dirname(globals()["\_\_file\_\_"])

    STATIC\_DOC\_ROOT = os.path.join(dirname, 'static\_media/')

    #In DATABASES replace:
	#'ENGINE': 'django.db.backends.',
	#'NAME': '',
	#with
	'ENGINE': 'django.db.backends.sqlite3',
	'NAME': os.path.join(dirname, 'sqlite3.db'),

    #Under TEMPLATE\_DIRS add:
	os.path.join(dirname, 'exampleapp/templates'),
	#Add this also if you want easy registration for your apps
	os.path.join(dirname, 'registration/templates'),

    #Under INSTALLED\_APPS, uncomment/add:
	'django.contrib.admin',
	'django.contrib.admindocs',
	'exampleapp',
	#If you want registration, also add this:
	'registration',

    #Final django-registration settings:
	ACCOUNT\_ACTIVATION\_DAYS = 7

    EMAIL\_USE\_TLS = True
	EMAIL\_HOST = 'smtp.gmail.com'
	EMAIL\_HOST\_USER = 'youremail@gmail.com'
	EMAIL\_HOST\_PASSWORD = 'yourpassword'
	EMAIL\_PORT = 587


I really like most conventions laid out in `Zachary Voase's blog`_, so I
go ahead and create the appropriate directories and files. (Note: I
don't follow all of his conventions, as you will see).

From the top level of your project:

.. code-block:: bash

	#Let's layout the directory structure first
	mkdir static\_media
	mkdir static\_media/css
	mkdir static\_media/img
	mkdir static\_media/js
	mkdir utils
	#This will make it so we can import from utils
	touch utils/\_\_init\_\_.py

    #You should always have a readme!!!
	touch README

    #And I like to include a doc or two with the project (usually just copied down from the wiki)
	mkdir docs



We should also go into urls.py to make the admin site available. We're
also going to make it easy to manage all of our urls for each app in
this file in a readable way.

.. code-block:: bash

	nano urls.py
	------

    #Uncomment all of these lines:

    # from django.contrib import admin
	# admin.autodiscover()
	# (r'^admin/doc/', include('django.contrib.admindocs.urls')),
	# (r'^admin/', include(admin.site.urls)),

    #Add this outside the parantheses of urlpatterns:
	urlpatterns += patterns('exampleapp.views',
	    #Add urls in here
	)



And finally, we need to set up the admin database (just answer all the
questions):

.. code-block:: bash

	python manage.py syncdb



Lastly, if you need it, you should install django-registration into your
app directory (Though at this point, django-registration is getting
quite old, so keep that in mind. Anyone want to help and fork it?)

.. code-block:: bash

	wget https://bitbucket.org/ubernostrum/django-registration/get/v0.7.tar.gz
	tar xf v0.7.tar.gz
	rm v0.7.tar.gz



Also, you may want to put your project under git source control, sync it
to GitHub, and add a dev and testing branch to the git project. (Steps
mostly taken from GitHub's help pages)

If you haven't already set your username and email, do so now:

.. code-block:: bash

	git config --global user.name "Git Guru"
	git config --global user.email gitguru@example.com



Now we need to initialize this directory as a git project and add all
our files to git. Again, this is from the top level of your project.
(This is a handy command, worth of an alias, such as 'ga' for git all,
on my machines)

.. code-block:: bash

	git init
	git add -A --ignore-errors



Now let's commit and get it up to the git server (by now you should have
`created your first git repo`_, and seen similar directions)

.. code-block:: bash

	git commit -m 'Initial commit'
	git remote add origin git@github.com:gitguru/example.git
	git push origin master



.. _Zachary Voase's blog: http://blog.zacharyvoase.com/2010/02/03/django-project-conventions/
.. _created your first git repo: https://github.com/repositories/new
