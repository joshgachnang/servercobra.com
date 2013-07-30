Ignore files in SVN
###################
:date: 2010-11-18 13:11
:author: Josh
:category: Articles
:tags: Tips
:slug: ignore-files-in-svn

**Platform(s)**: Linux with Subversion

Any server administrator worth his salt should have a configuration
management system of some kind. Some people prefer Puppet, Chef, etc,
but I’ve been enjoying the simplicity of SVN to store configuration
files and scripts on a private SVN server (many of which get published
to this site). However, since most of my configuration scripts are
written in Python, they generate annoying \*.pyc (from being compiled)
and .py~ (from being edited via Kate or gedit) files that get saved to
SVN when they don’t need to be. I couldn’t find a tutorial that didn’t
throw errors, so here’s my quick set of commands to accomplish this
easy, but crucial for sanity, task.

First, make sure you’re in an SVN controlled folder, containing the
files you want ignored by SVN. Then simply type

.. code-block:: bash

	svn propedit svn:ignore .



The final period is crucial, as it designates “this folder” in POSIX
operating systems (like Ubunutu). Now simply type in each thing you want
ignored, either explicitly naming files (ignore.txt) or using variables
(\*.pyc).

.. code-block:: bash

	\*.pyc
	\*~



That’s it! You can check which files are being included/excluded using
(note: there are two dashes before “no”)

.. code-block:: bash

	svn status –no-ignore



You can also list the ignored files by typing

.. code-block:: bash

	svn propget svn:ignore


