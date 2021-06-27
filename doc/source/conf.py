import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
import textfile


project = 'textfile'
copyright = '2021, kenjimaru <kendimaru2@gmail.com>'
author = 'kenjimaru <kendimaru2@gmail.com>'
release = textfile.__version__

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon'
]

templates_path = ['_templates']

language = 'en'

exclude_patterns = []


html_title = project
html_theme = 'haiku'
html_static_path = ['_static']
