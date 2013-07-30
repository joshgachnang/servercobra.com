Google Storage for Developers 
##############################
:date: 2010-11-07 17:53
:author: Josh
:category: Articles
:slug: google-storage-for-developers

I got invited to Google Storage for Developers a couple of days ago.
 From what I can tell, it is basically the same as Amazon S3, just a few
years later.  However, it has a Google spin to it.  It has fantastic
documentation (even though it's not publicly available), \ `good
libraries for Python`_, and right now, free storage/bandwidth.  Knowing
Google, it will also integrate very well with AppEngine, which is the
big differentiator between Amazon's offerings and Google's.  Google
AppEngine as a provides a managed platform to run Python and Java apps
on, while Amazon's EC2 is a full virtual server, where you install your
own stack of software and manage that stack on your own.  It is also
quite expensive for small projects (minimum of around $40 a month).
 AppEngine provides you some free resources (they say enough to run a
small to medium site), and the option to pay for more when you need it.
The choice is yours on which to use, and mostly hinges on whether you
need to run services other just Python/Java apps. Though, if you need a
cloud server, I'd recommend Rackspace, which is running this, and all my
other sites.

Since I'm now having a love affair with AppEngine, I think Google
Storage will be extremely useful. I was going to integrate S3 with Open
ProofBook for picture storage, but I was considering migrating the
project to AppEngine anyway.  I want to make it a multi-tenant hosted
application for photographers, much as I have MindTouch setup right now
for my multiple sites. I think it will be interesting to get a working
application using Google Storage up, so other people can benefit from my
code when it goes public.

.. _good libraries for Python: http://code.google.com/p/gsutil/source/browse/trunk/src/cloudreader/README.google
