# -*- coding: utf-8 -*-
from flask import Flask
from flask_cors import CORS

from router import api


# Instantiated object
app = Flask(__name__)

# Add the header field allowed by cross-domain requests: for all urls under /, all origins are allowed to access
CORS(app, resources={r"/*": {"origins": "*"}}, methods=['GET', 'POST'], supports_credentials=True)

# Flask_restful init
api.init_app(app)


if __name__ == '__main__':
    app.run()

