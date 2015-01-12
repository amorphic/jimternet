Title: Open Source: From Project to Product
Date: 2015-12-31 18:00
Author: James
Category: Musings
Tags: "Open Source", Python, Braubuddy
Slug:
Status: draft

In their seminal work [Getting Real][getting real], 37 Signals talk about [scratching your own itch][scratch your own itch] when on the lookout for a new project. Well I was itching to brew consistently tasty beer. And brewing consistently tasty beer requires reliable temperature control.

Sure there were thermostats for sale on Ebay for 100 bucks that could keep fermentation temperature consistent. But I could see the [limitations of these][braubuddy background] and knew that a software-based solution would provide the flexibility to do so much more.

Searching the web I was surprised by the lack of an effective Open Source solution that I could either employ or co-opt. So armed with a $5 USB thermometer and some Python-fu I wrote a script and a cron job to take regular temperature readings and record them to a text file.

This was to be the beginning of a long journey which would culminate in the release of a fully-realised Open Source product called [Braubuddy][braubuddy]. I would take a lot of unexpected detours and learn a lot on the way.

---

###The Tosr0x###

Periodically recording temperature readings was a good start. What I needed next was the means to control temperature as well as monitor it. With an old fridge and a heat belt already in my posession all that I required were a pair of programatically-controlled mains power sockets. They would allow me to turn on the fridge when the brew was getting too warm and turn on the heat belt when it was getting too cold.

Again I was surprised at the dearth of open, cost-effective solutions available. So I embarked on a sub-project to build a USB powerboard which could be controlled via Python. This ultimately resulted in a [Python package to control the 'tosr0x' family of relay modules][tosr0x blog] and [a post detailing how to build a USB powerboard based on one of these modules][powerboard blog].

<center>![tosr0x][tosr0x]</center>

Where I had expected to spend some money for an existing solution, I instead ended up spending time on building one.

###Thermostat Algorithms###

Now that I could take temperature readings *and* control heating/cooling all I needed was a thermostat algorithm to determine when to heat and when to cool.

I naively imagined that there might be a convenient package lurking somewhere in [PyPI][pypi] which would allow me to `import thermostat` and get on with the project. But once more I was disappointed and forced to roll my own. 

After a few test runs on a fermenter filled with water, (yawn!) I let my humble rig loose on a real brew. I watched the temperature readings slowly climb towards the configured threshold, then quickly drop back after the tosr0x' relay _clicked_ and my ancient fridge rumbled to life. Over the course of a week my fermentation temperature stayed with +/-1C of my target - I had a working solution!

###Project to Product###

It was around this time that I began to seriously consider growing my project into a fully-fledged product. That first successful brew solidified for me the notion that this was something useful which could prove valuable to others. I even came up with a name: _"Braubuddy"_.

But as it stood, Braubuddy was little more than a simple Python module called by a cron job. It lacked scheduling, packaging, documentation and a user interface. It also only supported one type of thermometer, (my $5 TemperUSB) and one type of environmental controller (the tosr0x).

If I was going to make Braubuddy into a useful tool that an average home-brewer could install and run on a Raspberry Pi, there was much I needed to do.

###CherryPy###

Braubuddy required a web interface and a built-in scheduling system to replace cron. I investigated many web frameworks and ultiamtely settled upon [CherryPy][cherrypy]; an extremely lightweight, Pythonic web framework which happens to provide functionality to schedule background tasks via its [Monitor plugin][monitor plugin].

<center>![cherrypy logo][cherrypy logo]</center>

As I became more familiar with CherryPy I found two of my product goals conflicting. I absolutely wanted Braubuddy to be extensible so that in the future myself or other contributers might add support for new kinds of hardware, new thermostat algorithms and new metric output destinations. But I also wanted Braubuddy to be simple to configure, requiring the user to edit only a single configuration file rather than `braubuddy.conf`, `thermostats.conf`, `outputs.conf` etc.

I eventually <s>hacked</s> creatively engineered a solution which allowed me to squeeze all of the config into a single file. But along the way I enocuntered a [bug][cherrypy bug] in the CherryPy config parser which scuppered my plans. Undeterred I dove into the CherryPy source, fixed the bug and submitted a [pull request][cherrypy pr], learning quite a bit about [Abstract Syntax Trees][abstract syntax trees] along the way.

Finally I needed a new CherryPy version incoporating my fix to be released. I gave XXX the project maintainer a little poke and helped with the docs. CherryPy 3.2.2 was released and Braubuddy was one step closer to a produciton release of its own!  

###TemperUSB###

Just as I caught a glimpse of the alpha release light at the end of the tunnel I encountered yet another road block. When running Braubuddy for extended periods my USB thermometer would eventually stop responding to polling.

Once again I rolled up my sleeves and dug into the source, this time of the [temper-python][temper-python github] project. [Patching this problem][temper-python pr] would ultiamtely lead to my becoming a major contributor te temper-python project and owner of the [PyPI][temper-python pypi] release process. I also learned a great deal more than I'd intended about [pyusb][pyusb].

###Javascript and NVD3###

I was down to the final flourishes now. Braubuddy was sporting a 'minimalist' web interface To really push Braubuddy beyond 

![braubuddy screenshot][braubuddy screenshot]

###Documentation###

All the was left now was documentation. Sigh.

<center>![braubuddy logo][braubuddy logo]</center>

---

Moving from a simple piece of It was at various times challenging, frustrating, interesting and rewarding.

* Producing a fully-fledged product was immensely satisfying. Polish!
* Be prepared to get your hands dirty with other projects, talk to maintainers and fix bugs yourself!
* You'll learn lots.

[getting real]:https://gettingreal.37signals.com
[scratch your own itch]:https://gettingreal.37signals.com/ch02_Whats_Your_Problem.php
[braubuddy background]:http://www.braubuddy.org/introduction.html#background
[braubuddy]:http://braubuddy.org
[braubuddy logo]:http://braubuddy.org/_static/bb_logo_128x128.png
[tosr0x blog]:http://jimter.net/controlling-a-tosr0x-usb-relay-module-using-python
[powerboard blog]:http://jimter.net/how-to-build-a-usb-powerboard-and-control-it-with-python
[tosr0x]: http://www.tinyosshop.com/image/cache/data/board_modules/TOSR02-1-228x228.jpg
[cherrypy]:http://cherrypy.org
[cherrypy logo]:https://bytebucket.org/cherrypy/cherrypy/raw/af84d55d090c96023018d6b8b9b105c12d58fbf5/visuals/cherrypy_logo_small.jpg
[monitor plugin]:http://cherrypy.readthedocs.org/en/latest/pkg/cherrypy.process.html?highlight=monitor#cherrypy.process.plugins.Monitor
[cherrypy bug]:https://bitbucket.org/cherrypy/cherrypy/issue/1302/config-value-declarations-fail-if-keyword
[abstract syntax trees]:http://en.wikipedia.org/wiki/Abstract_syntax_tree
[cherrypy pr]:https://bitbucket.org/cherrypy/cherrypy/pull-request/62/fix-for-1302-config-value-declarations
[temper-python github]:https://github.com/padelt/temper-python
[temper-python pr]:https://github.com/padelt/temper-python/pull/13
[temper-python pypi]:https://pypi.python.org/pypi/temperusb
[pyusb]:http://walac.github.io/pyusb/ 
[meta refresh]:http://en.wikipedia.org/wiki/Meta_refresh
[nvd3]:http://nvd3.org
[braubuddy screenshot]:http://braubuddy.org/_images/1.png

