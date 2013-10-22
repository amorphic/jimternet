Title: Switching The Jimternet From Wordpress to Pelican
Date: 2013-10-16 17:00
Author: James
Category: Projects
Tags: Pelican
Slug: switching-the-jimternet-from-wordpress-to-pelican

I've just finished migrating The Jimternet from Wordpress to [Pelican][Pelican], a static blog generator written in Python. There are already [plenty][pelican_post_1] [of][pelican_post_2] [posts][pelican_post_3] extolling the virtures of Pelican and static blogs in general, so I'll simply share why the static blog paradigm made sense in my circumstances.

For the uninitiated: dynamic [Content Managemnt Systems][cms] such as Wordpress re-generate html each time a page is requested, (caching notwithstanding). The web server hosting the blog does this by executing scripts which in turn read content from a database backend.

This is a powerful paradigm which allows for almost infinite complexity. But by their very nature, blogs are relatively static websites. A blogger composes a post such as this one, publishes it, then nothing changes until the next publication.

Recognising this, Static site generators such as Pelican produce a website composed entirely of html files. Content is authored in either [Markdown][Markdown] or [RST][RST] and the site's configuration is maintained in a single file. When a new piece of content is added, Pelican re-generates the entire site from scratch. The result is a directory of html files, ready to be uploaded to a web server for hosting. Those old enough to have created a website in the 1990's, may feel a vague
sense of deju-vu.

I made the switch to static site generation for a number of reasons:

**Site Security**

I became interested in alternatives to Wordpress after one of my hosted sites was hacked. While researching the best means of restoring the site in question, it became clear that my experience was relatively common amongst those using CMS such as Wordpress and Joomla, (I was hosting sites built upon both of these).

These ubiquitous CMS and their vast libraries of user-created plugins enable users to deploy complex websites quickly and easily. However a single vulnerability in platform or plugin is enough for the site to become compromised by a malicious user.
The vast installed base of CMS-backed sites make an attractive target for hackers and while Wordpress and its more popular plugins are updated frequently, all it takes is a single unpatched plugin for a site and its entire contents to be utterly vulnerable.

A static site eliminates such security concerns as no code is executed on the server.

**Post Composition**

I do most of my blogging on the train where Internet access is patchy at best, so seamless offline editing is a high priority.

I'm also very comfortable working at the command line, which is handy given that my coding/blogging weapon of choice remains an elderly [Eee901][Eee901] netbook, ([Crunchbang][Crunchbang] Linux runs so well on it that I really can't justify an upgrade). 

And while the Wordpress admin interface has come a long way since I first started using it circa-2007, it's never felt quite 'right' to compose posts directly in html, (or using a wysiwyg editor which spits out html). Writing github README files and JIRA comments in Markdown always felt like I had a lot more control of my content.  

As such, using vim to compose blog posts in Markdown is a natural fit for me.

**It's Python!**

Pelican is written in Python, programming my language of choice and one in which I'm reasonably competent. I also have some previous experience using the Jinja2 templating engine, which Pelican uses to define site templates. So down the line I'll be able to build my own themes or plugins should I so desire.

**Publication and Source Control**
Source control (git)
* Revision control
* Backups not required
* Can work on blog anywhere, just check out from github
* Committed changes -> publish via hooks

**Performance**
* Cheap, lightweight VPS
* Always knew that if a post went viral my blog would die
* Some wordpress plugins exist but only help a little
* Not complex if scaling required

**Time If Of The Essence***
* All of the above save time, which is ultimately my most valuable commodity. The whole point of the Jimternet is to blog *about* what I do, I don't want to spend all of my time maintaining the blog itself!

Now I'm familiar with the basics. When I get time I may look into themes, plugins etc..

[Pelican]: http://docs.getpelican.com
[pelican_post_1]: http://
[pelican_post_2]: http://
[pelican_post_3]: http://
[cms]: http://
[Markdown]: http://
[RST]: http://
[Eee901]: http://
[Crunchbang]: http://
