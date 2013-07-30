Intel's Guide to Eucalyptus 
############################
:date: 2010-11-07 17:54
:author: Josh
:category: Articles
:slug: intels-guide-to-eucalyptus

**Platform(s):**\ Ubuntu

It appears Intel is just as excited about using Eucalyptus for private
cloud computing as I am.  They have released a very in depth guide on
how to set up and maintain such a cluster. The tutorial is focused on
resellers and solution providers, but the Best Practices section is
definitely of use to anyone involved in private cloud computing.  The
tip comes from @\ `Swardley`_, a great resource of information and
articles on cloud computing.

The setup they describe is most certainly larger than nearly any home
application could require, (this cloud can host up to 128 virtual
machines and makes it public to the rest of the world) however the
design and best practices sections provide a fantastic resource.  They
also give the actual steps to build this system on Ubuntu, which is
extremely helpful if you want to build on top of the\ `Diskless
Tuturoial`_ I already provided.  The Intel paper goes on to provide you
with ways to set up separate storage servers, proxy servers, VPN, and a
host of other useful bits that could expand the usefulness of your
cloud.

If you already built or are considering building a cloud using
Eucalyptus and Ubuntu, I would highly advise \ `downloading the PDF from
Intel`_.

.. _Swardley: http://twitter.com/swardley
.. _Diskless Tuturoial: http://www.servercobra.com/2010/02/diskless-eucalyptus-cluster/
.. _downloading the PDF from Intel: http://software.intel.com/en-us/articles/intel-cloud-builder/
