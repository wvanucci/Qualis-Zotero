import os
import sys
sys.path.insert(0, os.path.abspath('../../qualis_zotero'))

project = 'qualis-zotero'
author = 'Seu Nome'
release = '0.1.0'
language = 'pt_BR'

extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    # ... outras extensões que você já tenha
]

# Para suportar arquivos .md
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}


templates_path = ['_templates']
exclude_patterns = []

html_theme = 'furo'
html_static_path = ['_static']
