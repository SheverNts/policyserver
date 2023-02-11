import policyserver.config as conf
from policyserver.core.data import DataLoader
from flask import Flask, request, Response, jsonify, make_response
from paste.translogger import TransLogger
import importlib
import sys
import json
from waitress import serve
import typing as t
from policyserver import log

inputs = request
data = {}


def about():
    return {"Name": "Policy Server", "Version": conf.VERSION}


default_routes = [
    {"rule": "/about", "endpoint": "about", "view_func": about},
]


class HttpServer(Flask):
    def __init__(self, routes, rule_data, rules):
        self.app = Flask(__name__)
        self.add_routes(default_routes + routes)
        self.rule_data = rule_data
        self.rules = rules

    def run(self, port, host):
        """
        start fun for app
        """
        # self.app.run(port=8081)
        serve(TransLogger(self.app), host=host, port=port)

    def add_routes(self, routes):
        """
        Add routes to flask object
        """
        for r in routes:
            log.debug("adding rules")
            log.debug(r)
            self.app.add_url_rule(
                r["rule"],
                endpoint=r["endpoint"],
                view_func=r["view_func"],
                methods=["POST"],
            )
        self.app.before_request(self.before_request_func)
        # self.app.after_request(self.after_request_func)

    def before_request_func(self):
        """
        Importing data base on the request before processing it
        """
        log.debug(request.path)
        data_name = request.path.split("/")[3]
        log.debug(f"data_name: {data_name}")
        self.rules[data_name].data = self.rule_data[data_name]
        log.debug(f"self.rules[data_name].data :{self.rules[data_name].data}")
        self.rules[data_name].inputs = request.get_json()
        log.debug(f"self.rules[data_name].inputs: {self.rules[data_name].inputs}")
