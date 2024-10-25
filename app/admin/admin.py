# app/admin/admin.py

from flask import Blueprint

admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/admin', methods=['GET'])
def admin_page():
    # Implement admin functionality here
    return "Admin Page"
