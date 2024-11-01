# app/admin/admin.py

from flask import Blueprint, render_template

admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/admin', methods=['GET'])
def admin_page():
    # Implement admin functionality here
    return render_template('admin.html')
