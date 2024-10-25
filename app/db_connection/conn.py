# app/db_connection/conn.py

import psycopg2
from flask import current_app, g, Flask


def init_db_connection(app: Flask):
    @app.before_request
    def before_request():
        try:
            g.db = psycopg2.connect(
                dbname=current_app.config['DB_NAME'],
                user=current_app.config['DB_USER'],
                password=current_app.config['DB_PASS'],
                host=current_app.config['DB_HOST'],
                port=current_app.config['DB_PORT']
            )
        except psycopg2.OperationalError as e:
            app.logger.error(f"Database connection failed: {e}")
            # Handle connection error gracefully
            g.db = None

    @app.teardown_request
    def teardown_request(exception):
        db = g.pop('db', None)
        if db is not None:
            db.close()


# Assuming you have an app instance somewhere:
app = Flask(__name__)
app.config['DB_NAME'] = 'care6'
app.config['DB_USER'] = 'postgres'
app.config['DB_PASS'] = 'jelszo'
app.config['DB_HOST'] = '34.89.97.10'
app.config['DB_PORT'] = 5432

init_db_connection(app)