# -*- coding: utf-8 -*-
#
# conf.py that works with my approach of using pandoc to convert markdown text
# to restrctured text. It was created by taking the file version # cd20cc5 at
# https://github.com/rtfd/readthedocs.org/blob/master/docs/conf.py and removing
# all the lines that didn't pertain to my files that I could see. Then I deleted
# the lines that caused the builds to fail one by one until it worked.
#
# Impetus was that I was looking for a way to have the copyright set properly
# but allow my normal (hack) approach to making the `.rst` files for sphinx work.
#
#
import os
import sys

from recommonmark.parser import CommonMarkParser

sys.path.insert(0, os.path.abspath('..'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "readthedocs.settings.sqlite")



sys.path.append(os.path.abspath('_ext'))
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
]
templates_path = ['_templates']

source_suffix = ['.rst', '.md']
source_parsers = {
    '.md': CommonMarkParser,
}

master_doc = 'README.md'
project = u'tophat2_and_bowtie_compatibility'
copyright = u'2017, Wayne Decatur'
author = u'Wayne Decatur (fomightez on Github)'
version = '1.0'
release = '1.0'
exclude_patterns = ['_build']
default_role = 'obj'
pygments_style = 'sphinx'



on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]



