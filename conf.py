# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'template project'
copyright = '2022, Pascal Molin'
author = 'Pascal Molin'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
        'sphinx_math_dollar',
        'sphinxcontrib.katex',
        'sphinxcontrib.rstprog',
        'sphinxcontrib.mathenv',
        'sphinxcontrib.bibtex',
        'sphinxcontrib.gp',
        'sphinx_gitstamp',
]

rstprog_debug = False
math_dollar_debug = False
gp_js_path = 'https://webusers.imj-prg.fr/~pascal.molin/static/gp.2.12'

gitstamp_fmt = "%b %d %Y"

mathenv_environments = [
        # (rst directive, output, latex env)
        ('def'  , 'Definition'    , 'definition')  ,
        ('th'   , 'Theorem'      , 'theorem')     ,
        ('prop' , 'Proposition'   , 'proposition') ,
        ('cor'  , 'Corollary'    , 'corollary')   ,
        ('lem'  , 'Lemma'         , 'lemma')       ,
        ('dem'  , 'Proof' , 'proof')       ,
        ('rem'  , 'Remark'      , 'remark')      ,
        ('ex'   , 'Example'       , 'example')     ,
        ('exo'  , 'Exercise'      , 'exercise')    ,
        ('sol'  , 'Solution'      , 'solution')    ,
        ('algo' , 'Algorithm'     , 'algorithm')   ,
]
mathenv_nonumber = [ 'dem', 'sol' ]

katex_options = r'''macros: {
  "\\im": "\\operatorname{Im}",
  "\\re": "\\operatorname{Re}",
  "\\N": "\\mathbb{N}",
  "\\Z": "\\mathbb{Z}",
  "\\Q": "\\mathbb{Q}",
  "\\A": "\\mathbb{A}",
  "\\R": "\\mathbb{R}",
  "\\C": "\\mathbb{C}",
  "\\F": "\\mathbb{F}",
  "\\k": "\\mathbb{k}",
  "\\K": "\\mathbb{K}",
  "\\H": "\\mathbb{H}",
  "\\ga": "\\mathfrak{a}",
  "\\gn": "\\mathfrak{n}",
  "\\gm": "\\mathfrak{m}",
  "\\gp": "\\mathfrak{p}",
  "\\gq": "\\mathfrak{q}",
  "\\ceil": "\\left\\lceil #1\\right\\rceil",
  "\\floor": "\\left\\lfloor #1\\right\\rfloor",
  "\\abs": "\\left\\lvert #1\\right\\rvert",
  "\\set": "\\left\\{ #1\\right\\}",
}'''

# Add any paths that contain templates here, relative to this directory.
#templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pascal'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
