from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from sqlalchemy import create_engine,Column,Integer,String,Boolean,Date
from sqlalchemy.orm import sessionmaker, declarative_base

app = FastAPI()

app.add_middleware(
    SessionMiddleware,
    secret_key="Mahadev_Bholenath_Shankar_180905_Kailash"
)

DATABASE_URL = "sqllite:///./tasks.db"

engine = create_engine(
    DATABASE_URL,
    connect_args = {"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush = False,
    bind= engine
)

Base = declarative_base()

class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True,index=True)
    title = Column(String(150), default=NULL)
    description = Column(String(300), default=NULL)
    priority = Column(String(20), default=NULL)
    is_complited = Column(Boolean, default=False)
    due_date = Column(Date, default=datetime.now)
    
Base.metadata.create_all(bind=engine)

print("Database successfully created")