# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

AUTHOR = 'sayo'
SITENAME = 'sayo'
SITELOGO = 'images/Novas_oc_with_smoke.jpg'
SITEURL = "https://sayo.gay"

PATH = "content"
THEME = 'theme'
#PAGE_PATHS = ["pages", "badges"]

#FEED_ALL_ATOM = "feeds/all.atom.xml"
#CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DISPLAY_HOME = False

DARK_LIGHT_SWITCHING_OFF = False

DELETE_OUTPUT_DIRECTORY = True

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# Following items are often useful when publishing

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""
