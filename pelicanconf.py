AUTHOR = 'sayo'
SITENAME = 'sayo'
SITELOGO = 'images/Novas_oc_with_smoke.jpg'
SITEDESCRIPTION = 'personal site, possibly a blog'


PATH = "content"
#STATIC_PATHS = ['badges', 'images']

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

THEME = 'theme'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

DISPLAY_HOME = False

DARK_LIGHT_SWITCHING_OFF = False

#ABOUT_URL = 'about'
#ABOUT_SAVE_AS = 'about/index.html'
#MENU_INTERNAL_PAGES = (
#    ('about', ABOUT_URL, ABOUT_SAVE_AS)
#)
PATH_METADATA = r"(?P<path_no_ext>.*)\..*"
#ARTICLE_URL = ARTICLE_SAVE_AS = PAGE_URL = PAGE_SAVE_AS = "{path_no_ext}.html"