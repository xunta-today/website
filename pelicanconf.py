#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "GaoJin"
SITENAME = "XunTA"
SITEURL = "https://xunta.today"
CDNSITEURL = (
    "https://cdn.jsdelivr.net/gh/xunta-today/pelican-themes@master/pelican-bootstrap3"
)
THEME_STATIC_DIR = "static"

PATH = "content"

TIMEZONE = "Asia/Shanghai"

DEFAULT_LANG = "en"

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
ARTICLE_EXCLUDES = ["html", "static"]
PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = [
    # "css-html-js-minify",
    "sitemap",
    "i18n_subsites",
    "related_posts",
    "tipue_search",
    "neighbors",
]

SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.5, "indexes": 0.5, "pages": 0.5},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
}

GOOGLE_ANALYTICS = "UA-153607218-1"


THEME = "pelican-bootstrap3"
JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}
I18N_TEMPLATES_LANG = "en"


DISPLAY_RECENT_POSTS_ON_SIDEBAR = True


DIRECT_TEMPLATES = ["index", "tags", "categories", "authors", "archives", "search"]

# SOCIAL = (
#     ("github", "http://github.com/jin10086/xunta2"),
#     ("zhihu", "https://www.zhihu.com/people/igaojin"),
#     ("weibo", "https://www.weibo.com/52kantu/home?wvr=5"),
# )

STATIC_PATHS = ["static"]
EXTRA_PATH_METADATA = {
    "static/404.html": {"path": "404.html"},
    "static/favicon.ico": {"path": "favicon.ico"},
}
SIDEBAR_ON_LEFT = True
ARCHIVES_SAVE_AS = "archives.html"
DISPLAY_CATEGORIES_ON_MENU = False
