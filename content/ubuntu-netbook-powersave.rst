Ubuntu Netbook PowerSave
########################
:date: 2010-11-18 12:26
:author: Josh
:category: Articles
:tags: Ubuntu
:slug: ubuntu-netbook-powersave

The first thing I do when I reinstall Ubuntu on my netbook is set up
power saving stuff (after getting the proprietary wifi drivers over
ethernet.....grr..).  Here's a handy way to make sure you enable power
saving features every time you boot the computer. We are going to create
a file called S99powersave in the /etc/rc5.d/ directory, which is a set
of scripts that gets run when going into runlevel 5 (the default Ubuntu
runlevel when you boot up).   S99 denotes the order in which the scripts
are run.  The lower numbers get executed first.  Since we want to be the
least intrusive as possible, we are going to put it as one of the last
scripts to be run. This could also be put into the file /etc/rc.local,
with similar results.

.. code-block:: bash

    sudo nano /etc/rc5.d/S99powersave


.. code-block:: bash

    # Enable power save for Intel audio devices
    echo 1 > /sys/module/snd\_hda\_intel/parameters/power\_save

    # Enable SATA link power management
    echo min\_power > /sys/class/scsi\_host/host0/link\_power\_management\_policy

    # Turn bluetooth off (adds 2 hours of life to my netbook, up to 9 hours total)
    /sbin/rfkill block bluetooth

    # Increase Virtual Memory dirty writeback time
    echo 1500 > /proc/sys/vm/dirty\_writeback\_centisecs

    # Enable wireless power management
    /sbin/iwconfig wlan0 power timeout 500ms



The way I found these commands was by installing and running powertop
for Ubuntu. It gives you an easy way to disable some stuff, and then the
command to make it happen. Please run it on your computer and add any of
the output powertop shows you, so we can have a more complete script!
