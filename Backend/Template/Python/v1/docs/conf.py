# -*- coding: utf-8 -*-

import os
import sys
from datetime import datetime

# 添加项目路径
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('../src'))

# -- 项目信息 -----------------------------------------------------------------
project = 'v1'
copyright = f'{datetime.now().year}, Your Name'
author = 'Your Name'

# 从 pyproject.toml 读取版本
try:
    import tomllib
    with open("../pyproject.toml", "rb") as f:
        pyproject = tomllib.load(f)
    version = pyproject["project"]["version"]
    release = version
except:
    version = '0.1.0'
    release = '0.1.0'

# -- 扩展配置 -----------------------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',        # 从 docstring 生成文档
    'sphinx.ext.napoleon',       # Google/Numpy 风格 docstring 支持
    'sphinx.ext.viewcode',       # 添加源代码链接
    'sphinx.ext.intersphinx',    # 链接到其他项目文档
    'sphinx.ext.todo',           # TODO 支持
    'sphinx.ext.coverage',       # 文档覆盖率
    'sphinx.ext.mathjax',        # 数学公式
    'sphinx.ext.githubpages',    # GitHub Pages 支持
    'sphinx_autodoc_typehints',  # 类型提示支持
    'myst_parser',               # Markdown 支持
]

# -- Napoleon 配置 ------------------------------------------------------------
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_use_keyword = True
napoleon_preprocess_types = False

# -- Autodoc 配置 -------------------------------------------------------------
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__',
    'show-inheritance': True,
}
autodoc_typehints = 'description'
autodoc_typehints_format = 'short'
autodoc_class_signature = 'mixed'

# -- 通用配置 -----------------------------------------------------------------
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
master_doc = 'index'
language = 'en'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
todo_include_todos = True

# -- HTML 主题配置 ------------------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'includehidden': True,
    'titles_only': False
}
html_static_path = ['_static']
html_css_files = ['custom.css']
html_js_files = []
html_show_sourcelink = True
html_show_sphinx = True
html_show_copyright = True

# -- 交叉引用配置 -------------------------------------------------------------
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'pandas': ('https://pandas.pydata.org/docs/', None),
}

# -- MyST 配置 ----------------------------------------------------------------
myst_enable_extensions = [
    'colon_fence',
    'deflist',
    'dollarmath',
    'linkify',
]
myst_heading_anchors = 3

# -- 自定义设置 ---------------------------------------------------------------
def skip_member(app, what, name, obj, skip, options):
    """自定义跳过某些成员"""
    if name.startswith('_') and not hasattr(obj, '__doc__'):
        return True
    return skip

def setup(app):
    app.connect('autodoc-skip-member', skip_member)