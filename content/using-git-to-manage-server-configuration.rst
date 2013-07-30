Using Git to Manage Server Configuration
########################################
:date: 2012-09-04 13:02
:author: Josh
:category: Articles
:tags: Git, server
:slug: using-git-to-manage-server-configuration

All servers should have their configuration saved into version control
somewhere. Many people use Puppet or Chef to manage their configuration.
That is a little more power than I need for a few home servers, so I use
git. I'm very familiar with it, and it works great. If I make a change
and it breaks something, I can just rollback the changes to a known
working state. This article outlines a basic way to host your
configuration files on BitBucket, which provides unlimited free, private
repositories. You could also host them on your own server, but this was
much easier for me. I create one repository per server (or set of
servers).

To follow this article, `please sign up for a BitBucket account`_ and
create a repository.

First, we need to create SSH keys to save to BitBucket for
authentication. You can skip the second line if you already created SSH
keys.

.. code-block:: bash

	sudo su
	ssh-keygen -t rsa
	# Copy this output to BitBucket as a new SSH key
	cat ~/.ssh/id\_rsa.pub



Now we need to install git, and create a folder to save all our
configurations in. We'll do this by symlinking the files we're using to
a folder as root.

.. code-block:: bash

	sudo apt-get install git-core
	mkdir ~/git
	cd ~/git
	git init
	# Create an account and repository at BitBucket, sub in your own username/repo name
	git remote add origin ssh://git@bitbucket.org/USERNAME/REPO.git



Now that we have the repository set up, let's add our first file. I'm
going to add my NFS exports file. You'll need to do this for each file.
You can commit separately, or symlink all the files then do the commits
at the end.

.. code-block:: bash

	# Repository is set up. Now let's add some stuff and commit it.
	mkdir ~/git/etc
	# Symlink
	ln -s /etc/exports etc/exports
	# Add everything
	git add -A
	# Commit with a commit message
	git commit -am "Adding NFS exports"
	# Push the master branch to the origin server (BitBucket)
	git push origin master



Finally, to help myself remember to commit, I am adding a reminder to
my bashrc. Every time I log in as root, I will receive a message if
there are uncommited files my git directory.

.. code-block:: bash

	nano ~/.bashrc
	-----
	# Add this to the end of the file
	# Check git status
	cd /root/git
	DIRTY=$(git status --porcelain 2>/dev/null\grep "^??" \wc -l)
	if [ $DIRTY != 0 ]; then
	    echo -e '\\E[47;31m'"\\033[1mGit changes in /root/git need to be commited.\\033[0m"
	fi

.. _please sign up for a BitBucket account: https://bitbucket.org/account/signup
