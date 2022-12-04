# -*- coding: utf-8 -*-
from flask import Blueprint

web = Blueprint(
    name='web',
    import_name=__name__,
    static_folder='static',
    static_url_path='/web/static',
    template_folder='templates'
)
from . import views
