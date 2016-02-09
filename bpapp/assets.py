# -*- coding: utf-8 -*-
"""Application assets."""
from flask_assets import Bundle, Environment

css = Bundle(
    'libs/bootstrap/dist/css/bootstrap.css',
    'css/style.css',
    # 'css/ct-paper.css',
    # 'css/bootstrap-datetimepicker.min.css',
    filters='cssmin',
    output='public/css/common.css'
)

js = Bundle(
    'libs/jQuery/dist/jquery.js',
    'libs/bootstrap/dist/js/bootstrap.js',
    'js/plugins.js',
    'js/moment-with-locales.min.js',
    # 'js/bootstrap-datetimepicker.min.js',
    # 'js/bootstrap-datepicker.js',
    # 'js/bootstrap-select.js',
    # 'js/ct-paper.js',
    # 'js/ct-paper-checkbox.js',
    # 'js/ct-paper-radio.js',
    filters='jsmin',
    output='public/js/common.js'
)

assets = Environment()

assets.register('js_all', js)
assets.register('css_all', css)
