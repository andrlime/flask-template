"""
API routes for root blueprint
"""

from http import HTTPStatus

from flask import Blueprint, Response
from flask_cors import cross_origin
from template.constants import VERSION
from template.flask.util import make_json_response

bp = Blueprint("root", __name__)


@bp.route("/", methods=["GET"])
@cross_origin(origins="*")
def get_root_page() -> Response:
    """
    Template route
    """

    return make_json_response(f"Hello world! version: {VERSION}", HTTPStatus.OK)
