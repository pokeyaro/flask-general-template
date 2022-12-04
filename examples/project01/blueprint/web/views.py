# -*- coding: utf-8 -*-
from . import web
from flask import render_template


@web.route('/index')
def index():
    context = {
        'title': 'BluePrint',
        'greeting': 'Hello Flask',
    }
    return render_template('index.html', **context)
