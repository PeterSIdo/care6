# app/data_output/output.py

from flask import Blueprint

output_bp = Blueprint('output', __name__)


@output_bp.route('/data/output', methods=['GET'])
def output_data():
    # Implement data output functionality here
    return "Data Output Page"