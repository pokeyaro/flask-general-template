# -*- coding: utf-8 -*-
from flask import Blueprint

open = Blueprint(
    name='open',
    import_name=__name__
)
from . import views
