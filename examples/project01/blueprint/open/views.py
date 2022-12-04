# -*- coding: utf-8 -*-
from . import open


@open.route('/register')
def register():
    return 'registration success'

