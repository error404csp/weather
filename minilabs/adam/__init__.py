from flask import Blueprint, Flask
# from adam import adam_bp

adam_bp = Blueprint(
    'adam_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)

from minilabs.adam import adam