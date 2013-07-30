Using Dictionary-Based Logging Outside Django
#############################################
:date: 2012-04-26 14:40
:author: Josh
:category: Articles
:tags: Django, Python
:slug: using-dictionary-based-logging-outside-django

If you haven't checked out `Django's logging facilities`_, do check them
out. They are invaluable! One place the Django test server fails at is
passing print statements to the console. Most production servers aren't
going to make print output available (or readily available), and too
much debugging code relies on print statements, instead of logging. You
can get the same effect as a print statement, along with logging to a
file, pretty easily.

However, when you're writing code outside of Django, or code that is
portable outside of Django (like some of my utility scripts), you need
these same abilities without the Django settings file. DictConfig allows
you to use Django-style logging, outside Django, but it was only
introduced in Python 2.7. Many servers are still on Python 2.6. Luckily,
you can just drop one extra file into your directory, and you're good to
go!

First, `download dictconfig.py`_. Put it into your project directory or
somewhere on your path.

Next, we'll configure a logger. We're going to have it capture all
message levels, and log them to both the console and a file in our
directory. This is the best combination and makes migrating to a
production server much easier.

.. code-block:: python

    import os
    import logging
    import dictconfig

    # PROJECT_ROOT is the folder you'll be logging to.
    PROJECT_ROOT='/home/josh/programming/project/'

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'handlers': {

            'file_log': {                 # define and name a second handler
                'level': 'DEBUG',
                'class': 'logging.FileHandler', # set the logging class to log to a file
                'formatter': 'verbose',         # define the formatter to associate
                'filename': os.path.join(PROJECT_ROOT, 'output.log')  # log file
            },
            'console':{
                'level':'DEBUG',
                'class':'logging.StreamHandler',
                'formatter': 'simple'
            },
        },
        'loggers': {
            'logger': {               # define another logger
                'handlers': ['file_log', 'console'],  # associate a different handler
                'level': 'DEBUG',                 # specify the logging level
                'propagate': True,
            },
        }
    }

    dictconfig.dictConfig(LOGGING)

Now when we want to log something, instead of "print 'Fire, exclamation
mark. Fire, exclamation mark. Help me, exclamation mark.'", we just do:

.. code-block:: python

    logging.critical('Fire, exclamation mark. Fire, exclamation mark. Help me, exclamation mark.')
    logging.error('Fire, exclamation mark. Fire, exclamation mark. Help me, exclamation mark.')
    logging.warning('Fire, exclamation mark. Fire, exclamation mark. Help me, exclamation mark.')
    logging.info('Fire, exclamation mark. Fire, exclamation mark. Help me, exclamation mark.')
    logging.debug('Fire, exclamation mark. Fire, exclamation mark. Help me, exclamation mark.')
    # Only within an exception handler:
    logging.exception('Fire, exclamation mark. Fire, exclamation mark. Help me, exclamation mark.')


There you go! Logging is easy!
Note: The Fire quote is from The IT Crowd, a hilarious TV show that
you should definitely check out. It is on Netflix!

.. _Django's logging facilities: https://docs.djangoproject.com/en/dev/topics/logging/
.. _download dictconfig.py: https://bitbucket.org/vinay.sajip/dictconfig/src/53b3c32dea46/src/dictconfig.py
