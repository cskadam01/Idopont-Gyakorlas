from sqlalchemy import Column, Integer, String, Date, create_engine
from sqlalchemy.orm import declarative_base

db_url= "mysql+pymysql://root:@localhost:3306/sqlalchemytest"

engine = create_engine(db_url)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    name = Column(String(50), unique=True)
    age = Column(Integer)
    password = Column(String(200))

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    maxSpace = Column(Integer)
    freeSpace = Column(Integer)




Base.metadata.create_all(engine)