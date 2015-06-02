from flask import Blueprint
from flask import render_template

from lazyblacksmith.cache import cache

home = Blueprint('home', __name__)

@home.route("/")
@cache.cached(timeout=3600*24)
def index():
    return render_template('base.html')