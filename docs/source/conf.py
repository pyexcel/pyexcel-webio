# -*- coding: utf-8 -*-
DESCRIPTION = (
    'A generic request and response interface for pyexcel web extensions.' +
    ''
)
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

intersphinx_mapping = {
    'pyexcel': ('http://pyexcel.readthedocs.org/en/latest/', None)
}
spelling_word_list_filename = 'spelling_wordlist.txt'
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'pyexcel-webio'
copyright = u'2015-2017 Onni Software Ltd.'
version = '0.0.10'
release = '0.0.11'
exclude_patterns = []
pygments_style = 'sphinx'
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'pyexcel-webiodoc'
latex_elements = {}
latex_documents = [
    ('index', 'pyexcel-webio.tex',
     'pyexcel-webio Documentation',
     'Onni Software Ltd.', 'manual'),
]
man_pages = [
    ('index', 'pyexcel-webio',
     'pyexcel-webio Documentation',
     [u'Onni Software Ltd.'], 1)
]
texinfo_documents = [
    ('index', 'pyexcel-webio',
     'pyexcel-webio Documentation',
     'Onni Software Ltd.', 'pyexcel-webio',
     DESCRIPTION,
     'Miscellaneous'),
]
