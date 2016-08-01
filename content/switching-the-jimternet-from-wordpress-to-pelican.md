Title: Switching The Jimternet From Wordpress to Pelican
Date: 2013-10-16 17:00
Author: James
Category: Projects
Tags: Pelican
Slug: switching-the-jimternet-from-wordpress-to-pelican
Status: published

I've just finished migrating The Jimternet from Wordpress to [Pelican][Pelican], a static blog generator written in Python. There are already [plenty][pelican_post_1] of [posts][pelican_post_2] extolling the virtures of Pelican and static blogs in general, so I'll simply share why the static blog paradigm makes sense for me.

For the uninitiated: dynamic [Content Managemnt Systems][cms] such as Wordpress re-generate html each time a page is requested, (caching notwithstanding). The web server hosting the site in question does this by executing scripts, which in turn read content from a database backend.

This is a powerful paradigm which allows for almost infinite complexity. But by their very nature, blogs are relatively static websites. A blogger composes a post, publishes it and then nothing changes until the next post is published.

Recognising this, Static site generators such as Pelican produce a website composed entirely of html files. Content is authored in either [Markdown][Markdown] or [RST][RST] and the site's configuration is maintained in a single file. When a new piece of content is added, Pelican re-generates the entire site from scratch. The result is a directory of html files, ready to be uploaded to a web server for hosting, (those old enough to have created a website in the 1990's may feel a vague
sense of deju-vu).

<!-- PELICAN_END_SUMMARY -->

I made the switch to static site generation for a number of reasons:

**Site Security**

I became interested in alternatives to Wordpress after one of my hosted sites was hacked. While researching the best means of restoring the site, it became clear that my experience was relatively common amongst those using CMS such as Wordpress and Joomla, (I was hosting sites built upon both of these).

These ubiquitous CMS and their vast libraries of user-created plugins enable users to deploy complex websites quickly and easily. However a single vulnerability in platform or plugin is enough for the site to become compromised by a malicious user.
The vast installed base of CMS-backed sites make an attractive target for hackers and while Wordpress and its more popular plugins are updated frequently, all it takes is a single unpatched plugin for a site and its entire contents to be utterly vulnerable.

Now that The Jimternet is static, I no longer have to worry about patching and vulnerable plugins.

**Post Composition**

I do most of my blogging on the train where Internet access is patchy at best, so seamless offline editing is a high priority.

I'm also very comfortable working at the command line, which is handy given that my coding/blogging weapon of choice remains an elderly [Eee901][Eee901] netbook, ([Crunchbang][Crunchbang] Linux runs so well on it that I can't really justify an upgrade). 

And while the Wordpress admin interface has come a long way since I first started using it circa-2007, it's never felt quite 'right' to compose posts directly in html, (or using a wysiwyg editor which in turn generates html). Writing github README files and JIRA comments in Markdown always made me feel that I had a lot more control over the content which I was creating.  

As such, using vim to compose blog posts in Markdown is a natural fit for me.

**It's Python!**

Pelican is written in Python, my language of choice and one in which I'm reasonably competent. I also have some previous experience using the Jinja2 templating engine, which Pelican uses to define site templates. So down the line I'll be able to build my own themes or plugins should I so desire.

**Publishing, Revision Control and Backups**

By adding my Pelican content directory to a [github repo] I'm able to maintain revisions of work-in-progress posts locally, even when I'm offline. When a post is ready to publish, I simply push it to origin. A [github service hook] initiates a git pull and subsequent Pelican update on my web server.

In this way I maintain a full revision history of my blog, negating the need for backups. And if I want to blog from a different computer I can just git clone my repo and start writing.

**Performance**

I host the Jimternet and my other sites on a modest Rackspace VPS. With some tweaking of Apache and Mysql this is adequate for hosting a CMS such as Wordpress or Joomla, provided I only get a few concurrent hits at any given time. But if perchance one of my posts appeared on a popular news site or was retweeted by somebody with a lot of followers, my poor little VPS wouldn't last long.

There are caching plugins for Wordpress that can help to absorb the impact of such an event, but nothing compares to the raw speed of serving static content. If I ever do need to scale, the process will be trivial and inexpensive compared to doing so with a database-backed CMS. My content could just as easily live on Amazon S3 or Rackspace Cloud Storage - there's even a new startup dedicated to [static hosting].

**Time If Of The Essence**

All of the reasons that I cite above are the basis of my main objective, which is to *save time*. As an engineer I want to maintain control of my blog rather than host it via wordpress.com or blogger.com. But time is my most valuable commodity and the whole point of The Jimternet is to blog *about* what I get up to. I don't want to spend all of my time maintaining the blog itself!

By switching to a static blog I've eliminated many of the time-sinks that were stealing away my precious productive hours. Now that I'm up and running with Pelican I hope to have the time to post more frequently, so stay tuned!

[Pelican]: http://docs.getpelican.com
[pelican_post_1]: http://jamesmurty.com/2013/05/23/migrate-wordpress-blog-to-static-site/
[pelican_post_2]: http://nicdumz.fr/blog/2010/12/why-blogofile/
[cms]: http://en.wikipedia.org/wiki/Content_management_system
[Markdown]: http://en.wikipedia.org/wiki/Markdown
[RST]: http://docutils.sourceforge.net/rst.html
[Eee901]: http://www.asus.com/Eee_Family/Eee_PC_901/
[Crunchbang]: http://crunchbang.org/
[github repo]: https://github.com/amorphic/jimternet
[github service hook]: https://help.github.com/articles/post-receive-hooks
[static hosting]: https://getforge.com/
