"""
Helper functions to make responses
"""

import http

from flask import Response, jsonify, make_response


def make_json_response(message: str, code: http.HTTPStatus) -> Response:
    """
    Encode a message into a JSONified response
    """

    return make_response(jsonify(message), code)
