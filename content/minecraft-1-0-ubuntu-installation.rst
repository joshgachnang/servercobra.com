Minecraft 1.0 Ubuntu Installation
#################################
:date: 2011-11-18 17:50
:author: Josh
:category: Articles
:tags: Minecraft, Ubuntu
:slug: minecraft-1-0-ubuntu-installation

The full version of Minecraft 1.0.0 was finally released today! You can
just updated your client, or install from scratch here.

-  `Client`_
-  `Server`_

Ubuntu Client Installation:

If you don't already have Minecraft installed, check this `Minecraft
Installation tutorial`_.

.. code-block:: bash

	# Backup your old client, just in case
	mv ~/.minecraft/bin/minecraft.jar ~/.minecraft/bin/minecraft.jar.bak
	# Download the new one
	cd ~/.minecraft/bin; wget https://s3.amazonaws.com/MinecraftDownload/launcher/minecraft.jar
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
	cd ~/minecraft; wget https://s3.amazonaws.com/MinecraftDownload/launcher/minecraft\_server.jar
	# Start minecraft again!
	startmc



.. _Client: https://s3.amazonaws.com/MinecraftDownload/launcher/minecraft.jar
.. _Server: https://s3.amazonaws.com/MinecraftDownload/launcher/minecraft_server.jar
.. _Minecraft Installation tutorial: http://www.servercobra.com/installing-minecraft-on-ubuntu/
