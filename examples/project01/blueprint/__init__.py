# -*- coding: utf-8 -*-
from flask import Flask

from .open import open
from .api import api
from .web import web


def create_app():
    app = Flask(__name__)
    app.debug = True

    app.register_blueprint(open, url_prefix='/open-api')
    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(web)

    return app
