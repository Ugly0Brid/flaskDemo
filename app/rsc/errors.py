from flask import jsonify
from . import rsc


@rsc.app_errorhandler(404)
def page_not_found(e):
    return jsonify({"status": -1, "error": 'no page was found'})


@rsc.app_errorhandler(500)
def internal_server_error(e):
    return jsonify({"status": -1, "error": 'internal error of the system'})
