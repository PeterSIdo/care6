# config.py
import os

class Config:
    # Example configuration settings, modify according to your needs
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DB_NAME = 'care6'
    DB_USER = 'postgres'
    DB_PASS = 'jelszo'
    DB_HOST = '34.89.97.10'
    DB_PORT = '5432'

    @staticmethod
    def get_db_uri():
        db_url = f"postgresql://{Config.DB_USER}:{Config.DB_PASS}@{Config.DB_HOST}:{Config.DB_PORT}/{Config.DB_NAME}"
        return db_url
