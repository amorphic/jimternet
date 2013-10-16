#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

AUTHOR = u'James Stewart'
SITENAME = u'The Jimternet'
SITEURL = 'http://jimter.net'
SITESUBTITLE = 'James Stewart Talks About Stuff'
TIMEZONE = 'Australia/Sydney'
DEFAULT_LANG = u'en'

RELATIVE_URLS = False
PAGE_DIR = 'pages'
DELETE_OUTPUT_DIRECTORY = True
DEFAULT_PAGINATION = 10

# Blogroll
"""
LINKS =  (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('You can modify those links in your config file', '#'),
)
"""

# Social widget
SOCIAL = (
        ('twitter', 'http://twitter.com/amorphic'),
)

# Feeds
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

# URLs
ARTICLE_URL = '{slug}/index.html'
ARTICLE_SAVE_AS = '{slug}/index.html'
CATEGORY_URL = 'categories/{slug}/index.html'
CATEGORY_SAVE_AS = 'categories/{slug}/index.html'

# External
DISQUS_SITENAME = "jimternet"
GOOGLE_ANALYTICS = "UA-1269813-2"
TWITTER_INTEGRATION_ENABLED = True
TWITTER_USERNAME = "amorphic"
