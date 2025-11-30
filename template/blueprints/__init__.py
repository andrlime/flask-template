"""
All blueprints imported in one module
"""

from typing import NamedTuple

from flask import Blueprint

from .root.api import bp as root


class BlueprintWrapper(NamedTuple):
    path: str
    blueprint: Blueprint


def all_blueprints() -> list[BlueprintWrapper]:
    return [
        BlueprintWrapper(path="", blueprint=root),
    ]
