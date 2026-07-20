# Configuration file for the Sphinx documentation builder.

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'MyProject'
copyright = '2026, Gianna Sophia Claros'
author = 'Gianna Sophia Claros'

# -- General configuration ---------------------------------------------------

extensions = [
    'myst_parser',
    'nbsphinx',
    'sphinx_rtd_theme',
]

master_doc = 'index'
# Allow both .rst and .md files as source
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# Templates path
templates_path = ['_templates']

# Exclude build and checkpoint files
exclude_patterns = ['_build', '**.ipynb_checkpoints']

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']