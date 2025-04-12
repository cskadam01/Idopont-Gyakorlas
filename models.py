from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, create_engine
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

db_url = "mysql+pymysql://root:@localhost:3306/gym_community"

engine = create_engine(db_url)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    age = Column(Integer)
    password = Column(String(200))
    email = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)

    # Kapcsolatok
    exercises = relationship("Exercise", back_populates="creator")
    progressions = relationship("Progression", back_populates="user")


class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    etype = Column(String(50))
    description = Column(Text)
    created_by = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.utcnow)

    creator = relationship("User", back_populates="exercises")
    progressions = relationship("Progression", back_populates="exercise")


class Progression(Base):
    __tablename__ = "progressions"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    exercise_id = Column(Integer, ForeignKey('exercises.id'))
    weight = Column(Integer)
    reps = Column(Integer)
    sets = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="progressions")
    exercise = relationship("Exercise", back_populates="progressions")


# Tábla létrehozás
Base.metadata.create_all(engine)
