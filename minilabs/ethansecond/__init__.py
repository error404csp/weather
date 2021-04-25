from flask import Blueprint

ethan2_bp = Blueprint(
    'ethan2_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)

from minilabs.ethansecond import ethan2