GitHub Setup Utility
####################
:date: 2010-12-30 00:08
:author: Josh
:category: Articles
:tags: GitHub, Script
:slug: github-setup-utility

Every 6 months or so, I wipe my computers and install the new version of
Ubuntu. And each time, I have to set up git and GitHub again. And every
time, I have to go find their support docs for just how to do it, which
is annoying. So I wrote a quick little utility that prompts for your
username and email, and gets all your keys and such ready for GitHub. It
even copies your public key to the clipboard, for easy pasting into the
GitHub key interface!

Download `Github Setup Utility`_.

And run it from the command line:

.. code-block:: bash

	sudo sh git\_setup.sh



Now test to make sure it worked.

.. code-block:: bash

	ssh git@github.com



You should get a congratulatory message about how awesome you are! If
you are running Ubuntu like me, and get "agent admitted failure to sign
using the key", simply reboot. It is a known (and apparently ignored???)
bug in Ubuntu.

.. _Github Setup Utility: http://ServerCobra.com/downloads/git_setup.sh
