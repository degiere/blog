#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Chris Degiere'
SITENAME = "Chris Degiere's Data Science Blog"
# SITEURL = ''

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
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/chrisdegiere'),
          ('Twitter', 'https://twitter.com/degiere'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins', './pelican-plugins']
PLUGINS = [
    'i18n_subsites',
    'series',
    'tag_cloud',
    'liquid_tags.youtube',
    'liquid_tags.include_code',
    'render_math',
	'ipynb.markup'
	]

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
IGNORE_FILES = [".ipynb_checkpoints"]  

THEME = 'pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'

I18N_TEMPLATES_LANG = 'en'

PYGMENTS_STYLE = 'default'

# https://github.com/getpelican/pelican-plugins/tree/master/tag_cloud
TAG_CLOUD_MAX_ITEMS = 6
