# -*- coding: utf-8 -*-
from flask import jsonify
from flask_restful import Resource, reqparse


parser = reqparse.RequestParser()
parser.add_argument('data', required=True, help='Data cannot be blank!')


class Hello(Resource):
    def get(self):
        result = {
            'code': 0,
            'data': {
                'greetings': 'Hello Flask',
            },
            'msg': 'success'
        }
        return jsonify(result)

