#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'David Bendet'
SITENAME = u'David Bendet'
SITEURL = 'www.davidbendet.com'
THEME = '/Users/dbendet/Documents/pelican_blog/themes/pelican-svbtle'
PATH = 'content'
AUTHOR_BIO_ONE = 'I do analytics at Etsy.'
# AUTHOR_BIO_TWO = 'I like Seinfeld and hockey.' #board games, idioms..

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Github', 'https://github.com/dbendet'),
         ('LinkedIn', 'https://www.linkedin.com/pub/david-bendet/40/3a1/685'),
         ('Twitter', 'https://twitter.com/dbendet'),
         ('Contact', 'mailto:dbendet@gmail.com'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 8

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
