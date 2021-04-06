from flask import Blueprint

ethan_bp = Blueprint(
    'ethan_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)

import ethan