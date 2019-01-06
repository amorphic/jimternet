#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'James Stewart'
SITENAME = 'Jimternet'
SITEURL = 'https://jimter.net'
SITESUBTITLE = 'The Personal Blog of James Stewart'

PATH = 'content'

TIMEZONE = 'Australia/Sydney'

DEFAULT_LANG = 'en'

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Links 
LINKS = (
)

# Social
SOCIAL = (('twitter', 'https://twitter.com/amorphic'),
          ('github', 'https://github.com/amorphic'),
          ('flickr','https://www.flickr.com/amorphic/'),
          ('envelope','mailto:james@amorphitec.io'))

DEFAULT_PAGINATION = 6

RELATIVE_URLS = False 

# Theme
THEME = 'attila'
HEADER_COVER = 'assets/images/sydney_drones.jpg'
ADDTHIS_PUBID = 'ra-58a643dd9da972b7'
STATIC_PATHS = ['assets']
EXTRA_PATH_METADATA = {
    'assets/favicon.ico': {'path': 'favicon.ico'},
}
FORMATTED_FIELDS = [
    'summary',
]
CSS_OVERRIDE = [
    'assets/css/jimternet_attila.css'
]

# Plugins
PLUGIN_PATHS = [
    'plugins',
]
PLUGINS = [
    'pelican_youtube',
    'summary',
    'tag_cloud',
]

# Tags
TAG_CLOUD_STEPS = 4

# External
DISQUS_SITENAME = 'jimternet'
GOOGLE_ANALYTICS = 'UA-1269813-2'
TWITTER_INTEGRATION_ENABLED = True
TWITTER_USERNAME = 'amorphic'

AUTHORS_BIO = {
  "james": {
    "name": "James",
    "cover": "assets/images/sydney_drones.jpg",
    "image": "https://avatars2.githubusercontent.com/u/1538480",
    "website": "https://jimter.net",
    "linkedin": "james-stewart-86a98b11",
    "twitter": "amorphic",
    "github": "amorphic",
    "location": "Woy Woy",
    "bio": "Technologist with over a decade of experience in IT Ops and an increasing focus on Software Design + Development. Maker and Open Source proponent/contributor with a life-long passion for technology and specialising in Linux, Python, IoT, 3D Printing and Monitoring. Co-founder of Amorphitec, Enstaved and SparkCC. Works remotely."
  }
}

