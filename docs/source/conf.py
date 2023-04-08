# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Property Managament System'
copyright = '2023, Jay Dev Jha'
author = 'Jay Dev Jha'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

html_static_path = ['_static']

html_css_files = [
    'css/custom.css',
]

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

extensions = ['sphinx.ext.graphviz']


# -- Options for EPUB output
epub_show_urls = 'footnote'
html_favicon = '_static/images/favicon.ico'
html_logo = "_static/images/first.png"
