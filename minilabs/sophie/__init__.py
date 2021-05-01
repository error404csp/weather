from flask import Blueprint

sophie_bp = Blueprint(
    'sophie_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)

from minilabs.sophie import sophie
from minilabs.sophie import bubble