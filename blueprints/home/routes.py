from flask import Blueprint, render_template
from models import Project

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def index():
    projects = Project.query.limit(3).all()
    return render_template('home/index.html', projects=projects)

@home_bp.route('/about')
def about():
    return render_template('home/about.html')
