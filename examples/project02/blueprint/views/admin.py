# -*- coding: UTF-8 -*-
from flask import Blueprint


admin = Blueprint('admin', __name__)

@admin.route('/bar')
def bar():
    return 'bar'

