Minecraft 1.9 Prerelease 6 Ubuntu Installation
##############################################
:date: 2011-11-11 13:51
:author: Josh
:category: Articles
:tags: Minecraft, Ubuntu
:slug: minecraft-1-9-prerelease-6-ubuntu-installation

Jeb tweeted the links to the 1.9.6 client and server today. The release
candidate should be out Sunday, so find those bugs! If you missed them,
here they are:

-  `Client`_
-  `Server`_

**Note:** This is outdated. `For the updated client, check this
page.`_
Ubuntu Client Installation:

.. code-block:: bash

	# Backup your old client, just in case
	mv ~/.minecraft/bin/minecraft.jar ~/.minecraft/bin/minecraft.jar.bak
	# Download the new one
	cd ~/.minecraft/bin; wget http://assets.minecraft.net/1\_9-pre6/minecraft.jar
	# And play like normal!
	minecraft
	# If you didn't alias this:
	java -Xmx1024M -Xms512M -cp Minecraft.jar net.minecraft.LauncherFrame

And for the Ubuntu-based server installation:

.. code-block:: bash

	# Stop the server
	stopmc
	# Or if you haven't followed my tutorials, get to your console (tmux or screen) and type "stop".
	# Backups are important!
	mv ~/minecraft/minecraft\_server.jar ~/minecraft/minecraft\_server.jar.bak
	# Get the new one
	cd ~/minecraft; http://assets.minecraft.net/1\_9-pre6/minecraft-server.jar
	# Start minecraft again!
	startmc

.. _Client: http://assets.minecraft.net/1_9-pre6/minecraft.jar
.. _Server: http://assets.minecraft.net/1_9-pre6/minecraft.jar
.. _For the updated client, check this page.: http://www.servercobra.com/minecraft-1-9-release-candidate-2-ubuntu-installation/
