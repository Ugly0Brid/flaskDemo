from flask import jsonify, request, json
from manage import logger
from app import db
from . import rsc
from .models import DataCenter


@rsc.route("/")
def index():
    return jsonify({"status": 0, "item_list": []})


@rsc.route("/list/<name>", methods=["GET"])
def list(name):
    item_list = [item._to_dict() for item in DataCenter.query.all()]
    return jsonify({"status": 0, "item_list": item_list})


@rsc.route("/create", methods=["POST"])
def create():
    data = request.data.decode()
    params = json.loads(data)
    data_center = DataCenter(**params)
    db.session.add(data_center)
    db.session.commit()
    return jsonify({"status": 0, "item_id": data_center.id})


@rsc.route("/update", methods=["POST"])
def update():
    data = request.data.decode()
    params = json.loads(data)
    id = params.get("id")
    params.pop("id")
    DataCenter.query.filter(DataCenter.id == id).first().update(**params)
    db.session.commit()
    return jsonify({"status": 0})


@rsc.route("/delete", methods=["POST"])
def delete():
    data = request.data.decode()
    params = json.loads(data)
    ids = params.get("ids")
    DataCenter.query.filter(DataCenter.id.in_(tuple(ids))).delete(synchronize_session=False)
    db.session.commit()
    return jsonify({"status": 0})
