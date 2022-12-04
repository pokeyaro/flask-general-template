# -*- coding: utf-8 -*-
from . import api


@api.route('/login')
def login():
    return 'login success'

