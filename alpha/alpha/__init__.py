from flask import Blueprint

alpha = Blueprint('alpha', __name__)

from . import route
from ..model import User
