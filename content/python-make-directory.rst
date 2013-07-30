Python: Make Directory
######################
:date: 2011-01-31 12:54
:author: Josh
:category: Articles
:tags: Python, Scripts
:slug: python-make-directory

As I read other people's Python code, I notice almost every project has
a utils.py file. I'm going to shamelessly post the most interesting (or
most useful) bits that I find, with proper credit. The first one is from
my work on modifying Gitosis to use a MySQL backend. Here's a quick way
to make a directory:

.. code-block:: python

	"""
	Create a new directory on a Unix system

    @param directory\_path
	@param (optional) permissions

    @exception OSERROR If directory cannot be made
	"""
	def mkdir(\*a, \*\*kw):
	    try:
	        os.mkdir(\*a, \*\*kw)
	    except OSError, e:
	    if e.errno == errno.EEXIST:
	        pass
	    else:
	        raise

Credit goes to the `Gitosis project.`_

.. _Gitosis project.: https://github.com/res0nat0r/gitosis
