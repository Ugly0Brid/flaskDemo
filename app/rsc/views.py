from flask import jsonify, request, json
from manage import logger
from app import db, redis_store
from . import rsc
from .models import DataCenter
from tasks import send_msg


@rsc.route("/")
def index():
    return jsonify({"status": 0, "item_list": []})


@rsc.route("/list/<name>", methods=["GET"])
def list(name):
    logger.info("bbbbbbbbbbbbbbbbbbbb")
    send_msg.delay(1, 2)
    redis_store.set('name', 'zfj')
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
    DataCenter.query.filter_by(id=id).update(params)
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
