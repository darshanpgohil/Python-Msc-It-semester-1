from sqlalchemy import Column, String, Integer, Date
from database import Base
from datetime import date

class Todo(Base):
    __tablename__ = "todos"
    # name: str
    # due_date: date
    # status: str
    
    id=Column(Integer, primary_key=True)
    name=Column(String, nullable=False)
    due_date=Column(Date, nullable=False)
    status=Column(String, nullable=False)