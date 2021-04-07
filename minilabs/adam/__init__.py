from flask import Blueprint

adam_bp = Blueprint(
    'adam_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)

from minilabs.adam import adam