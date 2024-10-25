# app/main/main.py

from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)


@main_bp.route('/main')
def home():
    return render_template('test.html')