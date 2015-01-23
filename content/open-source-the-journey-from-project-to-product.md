Title: Open Source: The Journey from Project to Product
Date: 2015-01-23 18:00
Author: James
Category: Projects 
Tags: "open source", python, braubuddy
Slug: open-source-the-journey-from-project-to-product 
Status: draft

In their seminal work [Getting Real][getting real], 37 Signals talk about [scratching your own itch][scratch your own itch] when looking for a new project. Well I was itching to brew consistently tasty beer. And brewing consistently tasty beer requires reliable temperature control.

Sure there were thermostats for sale on Ebay for 100 bucks that could keep fermentation temperature consistent. But I could see the [limitations of these][braubuddy background] and knew that a software-based solution would provide the flexibility to do so much more.

Searching the web I was surprised by the lack of an effective Open Source solution that I could either employ or co-opt. So armed with a $5 USB thermometer and some Python-fu I wrote a script and a cron job to take regular temperature readings and record them to a text file.

I didn't know it at the time, but this was to be the beginning of a long journey which would culminate in the release of a fully-realised Open Source product called [Braubuddy][braubuddy].

---

###The Tosr0x###

Periodically recording temperature readings was a good start. What I needed next was the means to control temperature as well as monitor it. With an old fridge and a heat belt already in my posession all that I required were a pair of programatically-controlled mains power sockets. They would allow me to turn on the fridge when the brew was getting too warm and turn on the heat belt when it was getting too cold.

Again I was surprised at the dearth of open, cost-effective solutions available. So I embarked on a sub-project to build a USB powerboard which could be controlled via Python. This ultimately resulted in a [Python package to control the 'tosr0x' family of relay modules][tosr0x blog] and [a post detailing how to build a USB powerboard based on one of these modules][powerboard blog].

<center>![tosr0x][tosr0x image]</center>

The [tosr0x.py][tosr0x github] sub-project has since proven quite popular thanks to a [link on the manufacturer's website][tosr0x tinysine]. It even inspired a [node.js version][tosr0x node]!

###Thermostat Algorithms###

Now that I could take temperature readings *and* control heating/cooling all I needed was a thermostat algorithm to determine when to heat and when to cool.

I naively imagined that there might be a convenient package lurking somewhere in [PyPI][pypi] which would allow me to `import thermostat` and get on with the project. But once more I was disappointed and forced to roll my own. 

After a few test runs on a fermenter filled with water, (yawn!) I let my humble rig loose on a real brew. I watched the temperature readings slowly climb towards the configured threshold, then quickly drop back after the tosr0x' relay _clicked_ and my ancient fridge rumbled to life. Over the course of a week my fermentation temperature stayed with +/-1°C of my target - I had a working solution!

###Project to Product###

It was around this time that I began to seriously consider growing my project into a fully-fledged product. That first successful brew solidified for me the notion that this was something useful which could prove valuable to others. I even came up with a name: _"Braubuddy"_.

But as it stood, Braubuddy was little more than a simple Python module called by a cron job. It lacked scheduling, packaging, documentation and a user interface. It also only supported one type of thermometer, (my $5 TemperUSB) and one type of environmental controller (the tosr0x).

If I was going to make Braubuddy into a useful tool that an average home-brewer could install and run on a Raspberry Pi, there was much I needed to do.

###CherryPy###

Braubuddy required a web interface and a built-in scheduling system to replace cron. I investigated many web frameworks and eventually settled upon [CherryPy][cherrypy]; an extremely lightweight, Pythonic web framework which happens to provide functionality to schedule background tasks via its [Monitor plugin][monitor plugin].

<center>![cherrypy logo][cherrypy logo]</center>

As I became more familiar with CherryPy I found two of my product goals conflicting. I absolutely wanted Braubuddy to be extensible so that in future myself or other contributers might add support for new kinds of hardware, new thermostat algorithms and new metric output destinations. But I also wanted Braubuddy to be simple to configure, requiring the user to edit only a single configuration file rather than `braubuddy.conf`, `thermostats.conf`, `outputs.conf` etc.

I eventually <s>hacked</s> creatively engineered a solution which allowed me to squeeze all of the config into a single file. But along the way I enocuntered a [bug][cherrypy bug] in the CherryPy config parser which scuppered my plans. Undeterred I dove into the CherryPy source, fixed the bug and submitted a [pull request][cherrypy pr], learning quite a bit about [Abstract Syntax Trees][abstract syntax trees] along the way.

Finally I contacted CherryPy maintainer [Jason Coombs][jason coombs] to request a release incoporating my bugfix and he kindly obliged with [CherryPy 3.3][cherrypy 3.3].

###Temper-Python###

Just as I caught a glimpse of the alpha release light at the end of the tunnel I encountered yet another road block. When running Braubuddy for extended periods my USB thermometer would eventually stop responding to Braubuddy's polling.

Once again I rolled up my sleeves and dug into the source, this time of the [temper-python][temper-python github] project. [Patching this problem][temper-python pr] would ultimately lead to my becoming a major contributor to the temper-python project and owner of its [PyPI][temper-python pypi] release process. I also learned a great deal more than I'd intended about [pyusb][pyusb].

###Making it Pretty###

I was down to the final flourishes now. Braubuddy was sporting a basic (_read: 'crap'_) web interface cunningly updated using a [meta refresh tag][meta refresh]. To really take Braubuddy from project to product I needed to present the environmental metrics in a clean and useful manner.

I revisited [Bootstrap] and leveraged its [glyphicons][bootstrap components] to label the metrics with pleasing minimalism. Then after evaluating several Javascript charting libraries I got to work learning [NVD3][nvd3]. Design isn't my forté but after a few layout iterations I had an interface I was happy with:

<center>![braubuddy screenshot][braubuddy screenshot]</center>

###Testing###

A lack of tests is a sure sign that a piece of Open Source software is more project than product. And Braubuddy's test suite was _far_ from comprehensive. As things stood it would be impossible to ensure that future changes didn't introduce bugs, particularly if those changes were contributions from other developers.
  
If I wanted users to trust Braubuddy to manage the temperature of their beer I needed to be able to update the codebase with confidence. So I spent time increasing test coverage and then configured automated testing via [travis][travis].

###Documentation###

Documentation is another area where Open Source projects are often found lacking. Few hackers find producing copy as engaging as writing code and after pouring blood, sweat and tears into a piece of software it can be tempting to hastily cobble together a `README` file and leave it at that.

I wanted to thoroughly document Braubuddy for two reasons:

1. To make it easy for new users to get started.
2. To make it easy for others to contribute code.

Fortunately Braubuddy's [docstrings][docstrings] were already in reasonable shape. All they required was some Sphinx [autodoc][sphinx autodoc] magic tied together with some basic install instructions and Braubuddy was [comprehensively documented][braubuddy]. This was yet another learning experience. For example before writing the Braubuddy docs I didn't know that [reStructuredText][restructuredtext] natively supports [tables][restructuredtext tables]. I do [now][sphinx tables]!

###Logo###

A logo adds legitimacy to a product. Braubuddy was feature-complete, tested, documented and ready for release but I really wanted to add a logo before I shared it with the world.

I asked my social network if anybody knew anybody who might create a basic logo. But designers willing to donate their time and skillset to creating logos for open-source projects seemed a little thin on the ground.

By this time I was itching to get a release out the door so I finally bit the bullet and learned the basics of [Inkscape][inkscape]. The result still smacks of "[programmer art][programmer art]" but it'll do until I can find that elusive designer...

<center>![braubuddy logo][braubuddy logo]</center>

---

I finally released Braubuddy in September 2014. Since then it's gathered a handful of [stargazers][braubuddy stargazers] and been downloaded a few thousand times. It has also assisted me in brewing many batches of consistently tasty beer...:).

Developing my simple project into a fully-realised product was at various times challenging, frustrating, interesting and rewarding. Ultimately the journey was one of the most satisfying experiences I've had applying my engineering skillset.

So if you've built something that you believe others might find useful I highly recommend you put in that [last 20%][pareto] of effort required to elevate it from project to product. You won't regret it! 

_**Last-minute update**: Around the time that I was finishing this post I read [a separate post by Nathan Marz describing the process of developing his Open-Source project "Storm" into a fully-fledged product][marz on storm]. His story is on a far more epic scale than mine but it touches on many of the same ideas._

[getting real]:https://gettingreal.37signals.com
[scratch your own itch]:https://gettingreal.37signals.com/ch02_Whats_Your_Problem.php
[braubuddy background]:http://www.braubuddy.org/introduction.html#background
[braubuddy]:http://braubuddy.org
[tosr0x blog]:http://jimter.net/controlling-a-tosr0x-usb-relay-module-using-python
[powerboard blog]:http://jimter.net/how-to-build-a-usb-powerboard-and-control-it-with-python
[tosr0x image]:http://www.tinyosshop.com/image/cache/data/board_modules/TOSR02-1-228x228.jpg
[tosr0x github]:https://github.com/amorphic/tosr0x
[tosr0x tinysine]:http://XXXX
[tosr0x node]:https://www.npmjs.com/package/tosr0x
[pypi]:http://www.pypi.prg
[cherrypy]:http://cherrypy.org
[cherrypy logo]:https://bytebucket.org/cherrypy/cherrypy/raw/af84d55d090c96023018d6b8b9b105c12d58fbf5/visuals/cherrypy_logo_small.jpg
[monitor plugin]:http://cherrypy.readthedocs.org/en/latest/pkg/cherrypy.process.html?highlight=monitor#cherrypy.process.plugins.Monitor
[cherrypy bug]:https://bitbucket.org/cherrypy/cherrypy/issue/1302/config-value-declarations-fail-if-keyword
[abstract syntax trees]:http://en.wikipedia.org/wiki/Abstract_syntax_tree
[cherrypy pr]:https://bitbucket.org/cherrypy/cherrypy/pull-request/62/fix-for-1302-config-value-declarations
[jason coombs]:https://bitbucket.org/jaraco
[cherrypy 3.3]:https://bitbucket.org/cherrypy/cherrypy/issue/1241/prepare-cp-33-release
[temper-python github]:https://github.com/padelt/temper-python
[temper-python pr]:https://github.com/padelt/temper-python/pull/13
[temper-python pypi]:https://pypi.python.org/pypi/temperusb
[pyusb]:http://walac.github.io/pyusb/ 
[meta refresh]:http://en.wikipedia.org/wiki/Meta_refresh
[bootstrap]:http://getbootstrap.com
[bootstrap components]:http://getbootstrap.com/components/
[nvd3]:http://nvd3.org
[braubuddy screenshot]:http://braubuddy.org/_images/1.png
[travis]:https://travis-ci.org/amorphic/braubuddy
[docstrings]:https://www.python.org/dev/peps/pep-0257/
[sphinx]:http://sphinx-doc.org
[sphinx autodoc]:http://sphinx-doc.org/ext/autodoc.html
[restructuredtext]:http://docutils.sourceforge.net/rst.html
[restructuredtext tables]:http://docutils.sourceforge.net/docs/user/rst/quickref.html#tables
[sphinx tables]:https://raw.githubusercontent.com/amorphic/braubuddy/master/docs/configure.rst
[braubuddy logo]:http://braubuddy.org/_static/bb_logo_128x128.png
[inkscape]:https://inkscape.org
[programmer art]:http://en.wikipedia.org/wiki/Programmer_art
[braubuddy stargazers]:https://github.com/amorphic/braubuddy/stargazers
[pareto]:http://en.wikipedia.org/wiki/Pareto_principle
[marz on storm]:http://nathanmarz.com/blog/history-of-apache-storm-and-lessons-learned.html
