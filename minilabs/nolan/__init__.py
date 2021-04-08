from flask import Blueprint

nolan_bp = Blueprint(
    'nolan_bp',
    __name__,
    template_folder='templates',
    static_folder='static',
)

from . import nolan