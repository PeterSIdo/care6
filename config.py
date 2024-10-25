import os


class Config:
    DB_NAME = os.getenv('DB_NAME', 'care6')
    DB_USER = os.getenv('DB_USER', 'postgres')
    DB_PASS = os.getenv('DB_PASS', 'jelszo')
    DB_HOST = os.getenv('DB_HOST', '34.89.97.10')
    DB_PORT = os.getenv('DB_PORT', '5432')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @classmethod
    def get_db_uri(cls):
        return f'postgresql://{cls.DB_USER}:{cls.DB_PASS}@{cls.DB_HOST}:{cls.DB_PORT}/{cls.DB_NAME}'