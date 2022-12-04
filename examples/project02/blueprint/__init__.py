# -*- coding: UTF-8 -*-
from flask import Flask, render_template

from .views.web import web
from .views.admin import admin


def create_app():
    app = Flask(__name__)
    app.secret_key = "4c6d5a1ba55625a1f6b06195628b7f8b"

    @app.route('/index')
    def index():
        return render_template('index.html')

    app.register_blueprint(web, url_prefix='/web')
    app.register_blueprint(admin, url_prefix='/admin')

    return app

