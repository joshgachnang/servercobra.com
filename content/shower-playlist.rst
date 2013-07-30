Shower Playlist
###############
:date: 2013-07-29 00:31
:author: Josh
:category: Articles
:tags: Android, Automation, Tasker
:slug: shower-playlist

I have a set of speakers in the bathroom that I use to play music and
podcasts while I shower. I had an extra NFC tag laying around, so I
decided to automate my music playing in the morning. With this, you walk
into the bathroom, plug the speakers into your headphone jack, put your
phone on the tag, and your morning playlist will start playing. Cool,
huh?

Here's what you need:

#. `An NFC tag`_
#. \ `Tasker`_ (costs $2.99, but definitely worth it)
#. `Auto Shortcut`_
#. `NFC Task Launcher`_
#. `Google Play Music`_ (I'm using All Access) and a playlist
#. Enable NFC on your phone. `Check here to see if your phone has
   NFC.`_ I'm using a Nexus 4.

Install all the apps above. In Tasker, go to Settings, Misc, and make
sure Allow External Access is checked. This will allow NFC Task Launcher
to launch tasker apps.

First, create a playlist in Google Play Music. I called mine...Morning.

In Tasker, go to the Tasks tab and hit the plus at the bottom. Let's
call this task "Shower". We're going to add a few steps that might not
be required, but work for me. Your mileage may vary. Add each of these
steps with the plus button at the bottom.

#. App -> Kill App -> Play Music
#. Plugin -> AutoShortcut -> Edit -> Music Playlist -> *Your Playlist
   Name*
#. Media -> Media Control -> Next -> Uncheck Simulate Media Button
#. If your phone is rooted, continue on. If not, this is as far as you
   can go. You might have to hit the play button on your playlist to get
   the music going.
#. Input -> Dpad -> Down
#. Input -> Dpad -> Select -> Repeat Times: 2

Now open up NFC Task Launcher.

#. Slide over to My Tasks and hit the plus button.
#. Select NFC as the trigger.
#. Name it "Shower" again
#. Hit the plus button to add an action
#. Select Tasker, Tasker Task, then hit next
#. Put in the name of your Tasker action ("Shower" in this example),
   then hit OK
#. Hit the arrow in the top corner.
#. Put your phone on your tag.
#. Once it says your tag has been read correctly, hit the checkmark in
   top right corner.

That's it! Now you can just add songs to your playlist via your
phone/web browser and you'll get a playlist in the morning.

Ideally, I'd like a pair of bluetooth speakers that pair and start
playing. That way, all you do is walk in, put the phone on the tag, and
you're done.

.. _An NFC tag: http://amzn.to/14cY1xW
.. _Tasker: https://play.google.com/store/apps/details?id=net.dinglisch.android.taskerm
.. _Auto Shortcut: https://play.google.com/store/apps/details?id=com.joaomgcd.autoshortcut&hl=en
.. _NFC Task Launcher: https://play.google.com/store/apps/details?id=com.jwsoft.nfcactionlauncher&hl=en
.. _Google Play Music: https://play.google.com/music/listen
.. _Check here to see if your phone has NFC.: http://www.nfcworld.com/nfc-phones-list/
