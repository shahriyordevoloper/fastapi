from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATEBASE = 'postgresql://postgres:test1234!@localhost:5432/Quizapp'

engine= create_engine(URL_DATEBASE)

SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base =declarative_base()