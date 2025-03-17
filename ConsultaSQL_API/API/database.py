from sqlalchemy import create_engine  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker  
  
# Reemplaza los valores con tus datos de conexión a MySQL  
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:12345.abcde@192.168.0.3:3308/CRM"  
  
engine = create_engine(SQLALCHEMY_DATABASE_URL)  
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  
  
Base = declarative_base()  
  
def get_db():  
    db = SessionLocal()  
    try:  
        yield db  
    finally:  
        db.close()  