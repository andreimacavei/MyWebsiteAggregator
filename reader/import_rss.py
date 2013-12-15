import re

from urllib2 import urlopen
from urlparse import urljoin, urlsplit
import json

from bs4 import BeautifulSoup, UnicodeDammit
from bs4.element import Tag

