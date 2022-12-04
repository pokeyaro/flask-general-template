# -*- coding: UTF-8 -*-
from flask import Blueprint

web = Blueprint('web', __name__)

@web.route('/foo')
def foo():
    return 'foo'

