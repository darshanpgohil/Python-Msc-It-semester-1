from sqlalchemy import Column, String, Integer, Date
from database import Base

class Todo(Base):
    __tablename__ = "todos"
    # name: str
    # due_date: date
    # status: str
    
    id=Column(Integer, primary_key=True)
    name=Column(String, nullable=False)
    due_date=Column(Date, nullable=False)
    status=Column(String, nullable=False)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username=Column(String, nullable=False)
    email=Column(String, nullable=False)
    password=Column(String, nullable=False)
    timestamp=Column(Date, nullable=False)
