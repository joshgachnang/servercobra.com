BASH: 32 or 64 bit check 
#########################
:date: 2010-11-09 17:12
:author: Josh
:category: Articles
:tags: BASH
:slug: bash-32-or-64-bit-check-2

Most packages that aren’t gotten through the default package manager are
compiled for a single architecture (x86, amd64, ARM, etc), therefore it
is useful to have a quick way to check whether the system is 32 or 64
bit, so an if statement can be used to do the appropriate action.

.. code-block:: bash

	#uname prints system info, like kernel, processor, etc. uname -m prints hardware name
	if [ $(uname -m) == "amd64" ]; then
	    ARCH=64
	else
	    ARCH=32
	fi



Now you can access $ARCH anywhere else in your program like so:

.. code-block:: bash

	if [ $ARCH == "32" ]; then
	    #Download 32 bit package
	else
	    #Download 64 bit package
	fi