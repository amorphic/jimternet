#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# blog info
AUTHOR = u'James Stewart'
SITENAME = u'The Jimternet'
SITEURL = ''
SITESUBTITLE = 'James Stewart - Making Stuff'
TIMEZONE = 'Australia/Sydney'
DEFAULT_LANG = u'en'

# Pelican Base
RELATIVE_URLS = True
PAGE_DIRS = [
    'pages',
]
DELETE_OUTPUT_DIRECTORY = True
DEFAULT_PAGINATION = 10

# Plugins
PLUGIN_PATHS = [
    '../pelican-plugins',
]
PLUGINS = [
    'pelican_youtube',
    'summary',
    'read_more_link',
]

# Read More
##SUMMARY_MAX_LENGTH = 50
READ_MORE_LINK = '<span>Read more...</span>'
READ_MORE_LINK_FORMAT = '<p><a class="read-more" href="/{url}">{text}</a></p>'

# Static Content
STATIC_PATHS = (['images'])

# Theme
THEME = 'pelican-clean-blog'
HEADER_COLOR = 'Gray'

# Formatting
SUMMARY_MAX_LENGTH = 50
FORMATTED_FIELDS = [
    'Summary',
    'Header_Cover',
]

# Blogroll
"""
LINKS =  (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('You can modify those links in your config file', '#'),
)
"""

# Social Widget
SOCIAL = (
        ('twitter', 'http://twitter.com/amorphic'),
        ('lastfm', 'http://lastfm.com/user/Jims101'),
        ('github', 'http://github.com/amorphic'),
)

# Feeds
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

# URLs
ARTICLE_URL = '{slug}'
ARTICLE_SAVE_AS = '{slug}/index.html'
CATEGORY_URL = 'categories/{slug}/'
CATEGORY_SAVE_AS = 'categories/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

# External
DISQUS_SITENAME = 'jimternet'
GOOGLE_ANALYTICS = 'UA-1269813-2'
TWITTER_INTEGRATION_ENABLED = True
TWITTER_USERNAME = 'amorphic'
