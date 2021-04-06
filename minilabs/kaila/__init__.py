from flask import Blueprint

kaila_bp = Blueprint(
    'kaila_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)

import kaila