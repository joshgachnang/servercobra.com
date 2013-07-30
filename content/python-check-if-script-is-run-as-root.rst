Python: Check if script is run as root
######################################
:date: 2010-11-08 20:58
:author: Josh
:category: Articles
:tags: Python
:slug: python-check-if-script-is-run-as-root

While I was translating one of my Bash scripts that was getting a bit
large and too heavy on using sed, I realized I need to translate some of
my scripts to Python also. So here's how to check if the script is being
run as root (useful for system maintenance scripts and the like).

.. code-block:: python

	import os
	import sys

    if not os.geteuid() == 0:
	    sys.exit('Script must be run as root')
