project = 'VOFTools'
author = 'Joaquín López'
copyright = '2026, Joaquín López'
version = '6'
release = '6'
language = 'en'
extensions = ['sphinx.ext.mathjax', 'sphinx.ext.githubpages']
root_doc = 'index'
exclude_patterns = []
html_theme = 'alabaster'
html_title = 'VOFTools 6 · User manual'
html_short_title = 'VOFTools 6'
html_static_path = ['_static']
html_css_files = ['voftools.css']
html_theme_options = {
 'description': 'Analytical and geometrical tools for VOF methods in arbitrary grids',
 'fixed_sidebar': True,
 'page_width': '1280px',
 'sidebar_width': '260px',
 'show_relbars': True,
}
html_sidebars = {'**': ['about.html', 'searchbox.html', 'navigation.html']}
html_show_sourcelink = True
html_copy_source = True
html_search_language = 'en'
html_permalinks_icon = '¶'
highlight_language = 'none'
mathjax3_config = {'tex': {'tags': 'none', 'macros': {'vec': ['\\boldsymbol{#1}', 1]}}}
templates_path = ['_templates']
mathjax_path = 'mathjax/es5/tex-mml-chtml.js'

html_baseurl = 'https://air-hpc.github.io/voftools-manual/'
