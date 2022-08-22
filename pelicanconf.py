AUTHOR = 'Gazali'
SITENAME = "Gazali's Website"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Jakarta'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing

CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None

FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
AUTHOR_FEED_RSS = 'feeds/%s.rss.xml'
RSS_FEED_SUMMARY_ONLY = False

# Blogroll
LINKS = (('Google Scholar', 'https://scholar.google.com/citations?user=cOyX2XYAAAAJ&hl=en'),
         ('SINTA id 6681756', 'https://sinta.kemdikbud.go.id/authors/profile/6681756'),
         ('Orcid id 0000-0001-7535-1057','#'),
         ('Scopus id', '#'))

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#Additional
DISPLAY_PAGES_ON_MENU = True
# DISPLAY_CATEGORY_ON_MENU = True

# PAGEORDERBY = 'date'
THEME='theme/Flex'
STATIC_PATHS = ['images']