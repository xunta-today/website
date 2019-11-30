#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "GaoJin"
SITENAME = "XunTA"
SITEURL = ""

PATH = "content"

TIMEZONE = "Asia/Shanghai"

DEFAULT_LANG = "zh-CN"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (
#     ("Pelican", "http://getpelican.com/"),
#     ("Python.org", "http://python.org/"),
#     ("Jinja2", "http://jinja.pocoo.org/"),
#     ("You can modify those links in your config file", "#"),
# )

# Social widget
# SOCIAL = (("You can add links in your config file", "#"), ("Another social link", "#"))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True


DEFAULT_CATEGORY = "xunta"
PAGE_EXCLUDES = ["html"]
PLUGIN_PATHS = ["/Users/gaojin/Documents/GitHub/pelican-plugins"]
PLUGINS = ["css-html-js-minify", "sitemap"]

SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.5, "indexes": 0.5, "pages": 0.5},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
}

GOOGLE_ANALYTICS = "UA-153607218-1"
