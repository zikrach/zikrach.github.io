#local_settings.py
# -*- coding: utf-8 -*-

AUTHOR = 'dimon'
SITENAME = 'About All!!!'
SITEURL = 'http://zzk.github.io'

TIMEZONE = 'Europe/Kiev'

LOCALE = 'ru_RU.UTF-8'
DEFAULT_LANG = 'ru'

# путь к исходникам
PATH = 'content'
# путь к выходным html-файлам
# в целом настройка не важна,
# ибо генерировать всё, кроме постов
# будем в корень проекта
OUTPUT_PATH = 'articles/'
# как сохранять посты
ARTICLE_URL = 'articles/{slug}.html'
# куда сохранять посты
ARTICLE_SAVE_AS = 'articles/{slug}.html'

RELATIVE_URLS = True # включать во время разработки
DISQUS_SITENAME = 'About All!!!'
PDF_GENERATOR = False
THEME = '/home/dima/blog/pelican-themes/bootstrap2'
CSS_FILE = 'style.css'
#OUTPUT_PATH = 'articles/'
#PATH = 'content'
WITH_PAGINATION = True
DEFAULT_PAGINATION = 10
DEFAULT_DATE_FORMAT = '%d %B %Y'
#ARTICLE_URL = 'articles/{slug}.html'
#ARTICLE_SAVE_AS = 'articles/{slug}.html'
NEWEST_FIRST_ARCHIVES = True
METADATA = u'About ALL!!!'

# Google analytics
#GOOGLE_ANALYTICS = 'UA-****'
#GOOGLE_ANALYTICS_DOMAIN = 'your_site_domain'

# Feeds
#FEED_ALL_ATOM = None
#FEED_ALL_RSS = None
#FEED_DOMAIN = 'your_site_domain'
#FEED_RSS = 'feeds/rss.xml'
#FEED_ATOM = 'feeds/atom.xml'
#FEED_MAX_ITEMS = 3

#Pages
DISPLAY_PAGES_ON_MENU  = False

# Social Links
SOCIAL = (('github', 'http://github.com/user'),
        ('twitter', 'http://twitter.com/user'),)
