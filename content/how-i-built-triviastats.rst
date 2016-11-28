How I Built TriviaStats.com
###########################
:date: 2015-4-14 11:00
:author: Josh
:category: Articles
:slug: how-i-built-triviastats

Every year, hundreds of teams and thousands of people gather near Stevens
Point, WI for the World's Largest Trivia Contest, hosted by the local
university radio station, WWSP. The contest is 54 hours long, with
questions broadcast over the radio and answers called in to a team of
highly caffeinated volunteers. Teams have the length of two songs
to answer questions, using any sources (thankfully including the
Internet). Questions range from fairly easy questions like
"An ad in a 1930's newspaper for this product reads '...', what is
the name of this product?" to "In the scene where $character and
$other_character are doing $thing, a train passes by in the background.
What does it say on the train?". Points are decided by how many teams
get a question correct. Scores are posted (almost) every hour. The only
problem is there's no way to get notified of when new scores get posted.
They're posted at random times throughout the hours, and our team often
didn't refresh for hours at a time. You can't see your score for previous
hours, so it's hard to tell how good or bad you've been doing.
So I wrote an website to fix that.

It started 4 years ago, when I was just learning Python and Django.
I wrote a basic scraper that would scrape once a minute, put it into
a Django model, and added a basic interface that would let you search
by team name or hour. Later, I added email text notifications when
scores were posted. This year, I decided to do a few more upgrades.

During our most recent monthly Hack Day, I decided it was time to learn
what modern frontend development looked like. Hack Days happen once a
month on the Friday after our office all-hands meeting. Developers are
encouraged to work on whatever interests them. Since I spend my whole
day writing backend code, I try to focus on frontend code and small apps
during Hack Day. I've written small apps,
home automation tools, an HTML music player using Amplitude controlled
by a Myo armband, and some projects more related to my day job.
I figured TriviaStats was a prime candidate for a rewrite.
So I spent a couple hours the night before researching what the new, hip
things were. To get started, I used Yeoman, which is a tool
that generates a blank project for you with all your dependencies
already configured. It cuts out the boilerplate. I choose:

* AngularJS, which I've been using in other side projects for a while
  now. It helps cut down on spaghetti code in Javascript, and is very
  batteries-included. For example, the Resource library is an excellent
  way to interact with REST APIs.
* Angular Material instead of Bootstrap or Foundation. Mobile-first
  is the name of the game, and Material Design looks great on mobile.
* Jade instead of HTML. No more '<' or '>' or even ending tags.
  You signify nesting with indents, which feels natural coming from
  Python.
* SCSS instead of straight CSS. Adds variables to your CSS, interesting
  nesting features, all while still being valid CSS. SASS is another
  step up, again using indentation instead of braces. I thought SCSS
  would be a slightly easier transition.
* Gulp to make building, testing, and developing easier. One command
  to build and deploy the app to production or testing. One other
  command launches the project in my browser window for development.
  The slickest part is BrowserSync, which synchronizes movement and
  clicks across multiple browsers and devices. So I launched it on
  3 browsers (one per screen), an iPhone, a Nexus 4, a Nexus 7, and an
  old Galaxy Tab 10.1 I got at Google IO. This really helped me focus
  on mobile optimization, rather than building in the browser and making
  sure it 'mostly works' on mobile. Combined with a watcher that
  automatically compiles my SCSS and Jade on the fly, the whole thing was
  fun to use. Highly recommended.
* Amazon S3 and Cloudfront deployment with gulp. In other side projects, I've served
  the frontend from the same container as the backend. This is bad for a
  couple reasons. Deployments take longer, because you have to build both
  the front and backend each time. Docker generally works best with a single
  service per container; serving both means having uWSGI and Nginx
  both running in the container. Configs are more complicated when they
  have to deal with both frontend and backend. Not ideal. Now deployments
  take about 10 seconds to build and deploy and then a few minutes
  to invalidate the index.html file in Cloudfront.
  CloudFront allows me to secure the entire frontend with SSL, along with
  putting the contest close to users.

Writing the frontend was a joy using these different tools. I don't think
I could go back now. The only major problem I ran into was Jade and
Angular have a conflict on the one time binding syntax (::variable), which
is a major performance gain for Angular. Jade simply wouldn't render it
in some instances, and I couldn't find a workaround. Very unfortunate.

The second upgrade was to put the app in Docker and write some simple config
management with Ansible to do deploys. The previous system was using
Fabric. It worked, but wasn't as simple as Ansible. It also helped
that I've been deploying my other side projects with Ansible and Docker
for a year now. You can check out the Dockerfile that runs TriviaStats
here [].

The third upgrade was to do the deployment in a scalable, redundant, monitored
way. While the load during Trivia isn't enough to require more than one
instance, having a bit of redundancy never hurts. I spun up a couple
Ubuntu 14.04 AWS instances behind an Elastic Load Balancer and enabled
CloudWatch monitoring. When I write a new version of the backend, I build
a new container, push it up to Docker Hub, and then run Ansible to pull
down the container, run database migrations, and start up the new
container. There's also an Nginx container on each server tha handles
SSL termination for the backend and configs to serve up the API. This
too is controlled by Ansible.

Lastly, I rewrote the backend mostly from scratch. It was originally serving up some
basic Django templates, with a bit of jQuery to make the site look like
it was developed this decade. I decided to switch to backend that is
only a REST API and the Django admin (which is one of the best parts of
Django). To handle the scores, there's a basic model, a serializer, and an
API view set. Subscribers are the same thing. There's also a scraper that
uses BeautifulSoup to parse the scores page and spit out some Scores
objects. I also made it pass PEP8 style checks and wrote some tests. It's
almost a proper project now.

I ran into a few problems with the site. I'm using ??Angular Django Resource.
It provides a handy API for dealing with Django REST Framework's.
However, I noticed it was automatically requesting the next page after it got
each response. Being that I have tens of thousands of scores, with a max
page size of 500, this isn't exactly ideal. I forked the project, removed
pagination for now (I'm not using it), and I'll figure out a real solution
later that I can contribute upstream, as I really like this library.

A somewhat frustrating problem with my Gulp setup is the templateCache.js is
not versioned. templateCache.js is where Angular HTML templates are stored
to prevent the frontend from having to make a new request for a template
each time you switch views or pages. Since it isn't versioned, it needs
to be invalidated every time it changes in Cloudfront, which takes 5-10
minutes. If I get that versioned, I'll be able to also version index.html,
and use the Cloudfront API to change which index.html is served up when
users first visit the site. This will take frontend deployments from 5-10
minutes (and a visit to the Cloudfront control panel) to 10 seconds and
a single command.
