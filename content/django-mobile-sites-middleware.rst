Mobile sites middleware
#######################
:date: 2010-11-17 16:19
:author: Josh
:category: Articles
:tags: Django, Python
:slug: django-mobile-sites-middleware

I love Django.  I also love CSS3.  Most of the sites that I'm developing
right now use CSS3, and therefore look terrible on many mobile devices
and Internet Explorer.  In this case, my options are either to make sure
every site gracefully falls back to IE-compatible HTML/CSS, or make a
separate site for the browser-impaired.  Well, call me malicious, but
I'm going to take the fast route and treat Internet Explorer users just
like mobile users and give them the less pretty (but still fully
functional) mobile site. I don't have the time make sure everything
looks good on standards compliant and non-compliant browsers, so
non-compliant desktop browsers (Internet Explorer, I'm looking at you)
and mobile phones are going to be treated the same way. Now the only
question is how to make Django do this easily.

My implementation uses two parts: a middleware and a wrapper for the
Django shortcut render\_to\_response. I'm pretty sure this could be
compacted down into a single middleware file, but I wanted a wrapper for
render\_to\_response anyway, so that it passes in all my
context\_processor and user variables in each view.

mobile\_middleware.py

.. code-block:: python

	MOBILE\_USERAGENTS = ("2.0
    MMP","240x320","400X240","AvantGo","BlackBerry",
	"Blazer","Cellphone","Danger","DoCoMo","Elaine/3.0","EudoraWeb",
	"Googlebot-Mobile","hiptop","IEMobile","KYOCERA/WX310K","LG/U990",
	"MIDP-2.","MMEF20","MOT-V","NetFront","Newt","Nintendo Wii","Nitro",
	"Nokia","Opera Mini","Palm","PlayStation Portable","portalmmm","Proxinet",
	"ProxiNet","SHARP-TQ-GX10","SHG-i900","Small","SonyEricsson","Symbian OS",
	"SymbianOS","TS21i-10","UP.Browser","UP.Link","webOS","Windows CE",
	"WinWAP","YahooSeeker/M1A1-R2D2","iPhone","iPod","Android",
	"BlackBerry9530","LG-TU915 Obigo","LGE VX","webOS","Nokia5800",)

    user\_agents\_test = ("w3c ", "acs-", "alav", "alca", "amoi", "audi",
	"avan", "benq", "bird", "blac", "blaz", "brew",
	"cell", "cldc", "cmd-", "dang", "doco", "eric",
	"hipt", "inno", "ipaq", "java", "jigs", "kddi",
	"keji", "leno", "lg-c", "lg-d", "lg-g", "lge-",
	"maui", "maxo", "midp", "mits", "mmef", "mobi",
	"mot-", "moto", "mwbp", "nec-", "newt", "noki",
	"xda", "palm", "pana", "pant", "phil", "play",
	"port", "prox", "qwap", "sage", "sams", "sany",
	"sch-", "sec-", "send", "seri", "sgh-", "shar",
	"sie-", "siem", "smal", "smar", "sony", "sph-",
	"symb", "t-mo", "teli", "tim-", "tosh", "tsm-",
	"upg1", "upsi", "vk-v", "voda", "wap-", "wapa",
	"wapi", "wapp", "wapr", "webc", "winw", "winw",
	"xda-",)

    import re

    class MobileDetectionMiddleware(object):
        """
        Useful middleware to detect if the user is
        on a mobile device.
        """

        def process\_view(self, request, view\_func, view\_args, view\_kwargs):
            is\_mobile = False;

            if request.META.has\_key('HTTP\_USER\_AGENT'):
                user\_agent = request.META['HTTP\_USER\_AGENT']

            # Test common mobile values.
            pattern =
                "(up.browser\|up.link\|mmp\|symbian\|smartphone\|midp\|wap\|phone\|windowsce\|pda\|mobile\|mini\|palm\|netfront)"
            prog = re.compile(pattern, re.IGNORECASE)
            match = prog.search(user\_agent)

            if match:
                is\_mobile = True;
                else:
                # Nokia like test for WAP browsers.
                # http://www.developershome.com/wap/xhtmlmp/xhtml\_mp\_tutorial.asp?page=mimeTypesFileExtension

            if request.META.has\_key('HTTP\_ACCEPT'):
                http\_accept = request.META['HTTP\_ACCEPT']

            pattern = "application/vnd\\.wap\\.xhtml\\+xml"
            prog = re.compile(pattern, re.IGNORECASE)

            match = prog.search(http\_accept)

            if match:
                is\_mobile = True

            if not is\_mobile:
                # Now we test the user\_agent from a big list.
                if user\_agent in MOBILE\_USERAGENTS:
                    is\_mobile = True

            test = user\_agent[0:4].lower()
            if test in user\_agents\_test:
                is\_mobile = True

            request.is\_mobile = is\_mobile


Create this file in the top directory of your project (the same folder
as urls.py). Then in add it to settings.py:

.. code-block:: python

	MIDDLEWARE\_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.middleware.csrf.CsrfResponseMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.http.ConditionalGetMiddleware',
	'django.middleware.gzip.GZipMiddleware',
	'mobile\_middleware.MobileDetectionMiddleware',
	)
	

This will activate the middleware. Now anywhere in your views, you can
use request.is\_mobile, which will be set to either True or False.

Now let's write the render\_to\_response wrapper. Put this at the top of
your views.py wherever you want to use it.

.. code-block:: python

	def short\_render(req, \*args, \*\*kwargs):
        kwargs['context\_instance'] = RequestContext(req)
        template = args[0]
        template = 'mobile\_' + template
        print template
        if req.is\_mobile:
            return render\_to\_response(template, args[1])
        else:
            return render\_to\_response(\*args, \*\*kwargs)
	

Now anytime you want to render a template, simply do it like this:

.. code-block:: python

	return short\_render('template.html', {'form': form})
	

And it will render template.html for compliant browsers and
mobile\_template.html for IE/mobile browsers.

If you want to make this work for only mobile browsers, simply remove
the statements marked off by #IE Detection.

**Added 12/1/10**

While using this on my own site, I found it would be very nice for the
simple templates (such as the about page) to just choose which base
template file they extend.  First, I created a standard, desktop
base.html file, and then a mobile friendly (with jQuery Alpha)
mobile\_base.html. If you have the above working, simple create a
mobile\_template\_processor.py in the root of your project:

.. code-block:: python

	def MobileTemplate(request):
	    if request.is\_mobile:
	        return {'extend\_base': 'mobile\_base.html'}
	    else:
	        return {'extend\_base': 'base.html'}

Now let's install our new template processor in settings.py:

.. code-block:: python

	TEMPLATE\_CONTEXT\_PROCESSORS = (
	"django.contrib.auth.context\_processors.auth",
	"django.core.context\_processors.request",
	"django.core.context\_processors.debug",
	"django.core.context\_processors.i18n",
	"django.core.context\_processors.media",
	"django.contrib.messages.context\_processors.messages",
	"mobile\_template\_processor.MobileTemplate",
	)


Now, to use this in a template, simply add this to the top:

.. code-block:: python

	{% extends extend\_base %}
	#Instead of this
	{% extends "base.html" %}
	
