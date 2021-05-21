from flask import Blueprint

nolan_bp = Blueprint(
    'nolan_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)

from minilabs.nolan import nolan
from minilabs.nolan import testpage