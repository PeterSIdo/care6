from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def connect_to_db():
    # Database connection details
    host = "35.224.207.195"
    port = "5432"
    dbname = "carerecords1"
    user = "postgres"
    password = "jelszo"
    # Create the database URL
    postgres_db_url = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"
    # Create the SQLAlchemy engine
    engine = create_engine(postgres_db_url)
    # Create a configured "Session" class
    session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    # Return the session_local class
    return session_local()

def get_db():

    session_local = connect_to_db()  # Get the SessionLocal class
    db = session_local
    try:
        yield db
    finally:
        db.close()