Bash Alias for Python/Virtualenv
################################
:date: 2012-01-21 13:10
:author: Josh
:category: Articles
:tags: BASH, Python
:slug: bash-alias-for-pythonvirtualenv

If you are writing Python apps, you should definitely be using
virtualenv. It creates an isolated virtual environment (hence the name),
where you can install Python apps without affecting the rest of the apps
on your machine. For example, if I have a website that relies on Django
1.2, and other sites that rely on Django 1.3, I can put them in
virtualenvs and just install the correct package versions in each. This
can also be applied to running different Python versions per project as
well, such as 2.5 for one and 3.0 in another. Yet another great use of
virtualenvs is testing your code in multiple version of Python.

Sold yet? Good! The only thing I find tedious about virtualenvs is
constantly typing long commands to activate a virtualenv. The common
command is:

.. code-block:: bash

	source ~/programming/project/bin/activate



That's more than I want to type each time. So let's make it an alias!
Simply replace PROJECT with the name of your project. Note: This assumes
you place all your projects in your home directory under a directory
called "programming". Modify that to meet your needs.

.. code-block:: bash

	echo 'alias PROJECT="source $HOME/programming/PROJECT/bin/activate" ' >> ~/.bash\_aliases

    # Or if you want to also move to the directory:
	echo 'alias PROJECT="source ~/programming/PROJECT/bin/activate; cd ~/programming/PROJECT" ' >> ~/.bash\_aliases

    bash



Well that's pretty cool. Now you just type whatever your project name
is, and the alias will activate the virtualenv so you can get to work.
If you use the second option, it will also move you into the project
directory. What if you have 30+ Python projects, like me? Do you really
want to write an alias for each one, and create a new one each time you
make a new project? I don't, so I'll write a simple function to take
care of it. Put this in your ~/.bash\_aliases (or the bottom of
~/.bashrc if you really want).

.. code-block:: bash

	# Python virtualenv
	SRC\_DIRECTORY="$HOME/programming"
	venv () {
	    source $SRC\_DIRECTORY/$1/bin/activate;
	    cd $SRC\_DIRECTORY/$1;

        # Then run "bash" again to reload the file, and you're done!
	}



To run it, simply type "venv PROJECT" into bash. It will activate the
environment and move you to the project directory. You can change
SRC\_DIRECTORY to whatever you want.
