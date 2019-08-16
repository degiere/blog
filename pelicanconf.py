#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Chris Degiere'
SITENAME = "Chris Degiere's Data Science Blog"
# SITEURL = 'https://degiere.github.io/blog'

# Set the article URL
# ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_URL = 'blog/{slug}/'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),)

SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/chrisdegiere'),
          ('Twitter', 'https://twitter.com/degiere'),
          ('Github', 'https://github.com/degiere'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

PLUGIN_PATHS = ['./plugins', './pelican-plugins']
PLUGINS = [
    'i18n_subsites',
    # 'series',
    'tag_cloud',
    # 'liquid_tags.youtube',
    # 'liquid_tags.include_code',
    # 'render_math',
    'ipynb.markup'
]

# https://docs.getpelican.com/en/stable/settings.html
SUMMARY_MAX_LENGTH = 100

# https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3
SHOW_ARTICLE_AUTHOR = False
THEME = 'pelican-themes/pelican-bootstrap3'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
BOOTSTRAP_THEME = 'flatly'
I18N_TEMPLATES_LANG = 'en'
PYGMENTS_STYLE = 'default'
HIDE_SIDEBAR = True

# https://github.com/danielfrg/pelican-ipynb
MARKUP = ('md', 'ipynb')
IGNORE_FILES = [".ipynb_checkpoints"]

# https://github.com/getpelican/pelican-plugins/tree/master/tag_cloud
TAG_CLOUD_MAX_ITEMS = 6

