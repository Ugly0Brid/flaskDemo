from flask import jsonify

from . import auth
from .models import Auth


@auth.route("/")
def index():
    auth = Auth.query.first().id
    return jsonify({"status": 0, "item_list": [{"a": 0, "auth_id": auth}]})


@auth.route("/aa")
def test():
    return jsonify({"status": 0})
